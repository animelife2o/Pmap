import socket
import threading
import argparse
import sys
from datetime import datetime

class Pmap:
    def __init__(self):
        self.target = ""
        self.ports = []
        self.open_ports = []
        self.scan_type = "tcp"  # Default scan type
        self.timeout = 1  # Socket timeout in seconds
        self.threads = []
        self.max_threads = 1000
        self.verbose = False

    def set_target(self, target):
        """Set the target IP or hostname"""
        self.target = target

    def set_scan_type(self, scan_type):
        """Set the scan type (tcp/udp)"""
        if scan_type.lower() in ["tcp", "udp"]:
            self.scan_type = scan_type.lower()
        else:
            raise ValueError("Scan type must be 'tcp' or 'udp'")

    def set_timeout(self, timeout):
        """Set socket timeout in seconds"""
        self.timeout = timeout

    def set_max_threads(self, max_threads):
        """Set maximum number of concurrent threads"""
        self.max_threads = max_threads

    def set_verbose(self, verbose):
        """Enable/disable verbose output"""
        self.verbose = verbose

    def add_port_range(self, start_port, end_port):
        """Add a range of ports to scan"""
        self.ports.extend(range(start_port, end_port + 1))

    def add_port_list(self, port_list):
        """Add a list of ports to scan"""
        self.ports.extend(port_list)

    def scan_port(self, port):
        """Scan a single port"""
        try:
            if self.scan_type == "tcp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            else:  # UDP
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            sock.settimeout(self.timeout)
            
            if self.scan_type == "tcp":
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    service = self.get_service_name(port)
                    self.open_ports.append((port, service))
                    if self.verbose:
                        print(f"Port {port} is open ({service})")
                sock.close()
            else:  # UDP scan (simplified - real UDP scanning is more complex)
                sock.sendto(b"test", (self.target, port))
                try:
                    data, _ = sock.recvfrom(1024)
                    service = self.get_service_name(port)
                    self.open_ports.append((port, service))
                    if self.verbose:
                        print(f"Port {port} is open|filtered ({service})")
                except socket.timeout:
                    # With UDP, no response usually means the port is open|filtered
                    service = self.get_service_name(port)
                    self.open_ports.append((port, "open|filtered/" + service))
                    if self.verbose:
                        print(f"Port {port} is open|filtered ({service})")
        except Exception as e:
            if self.verbose:
                print(f"Error scanning port {port}: {str(e)}")

    def get_service_name(self, port):
        """Get common service name for a port"""
        services = {
            20: "FTP Data",
            21: "FTP Control",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            67: "DHCP Server",
            68: "DHCP Client",
            69: "TFTP",
            80: "HTTP",
            110: "POP3",
            119: "NNTP",
            123: "NTP",
            143: "IMAP",
            161: "SNMP",
            194: "IRC",
            443: "HTTPS",
            465: "SMTPS",
            587: "SMTP (Submission)",
            993: "IMAPS",
            995: "POP3S",
            1433: "MSSQL",
            1521: "Oracle DB",
            3306: "MySQL",
            3389: "RDP",
            5432: "PostgreSQL",
            5900: "VNC",
            8080: "HTTP Proxy"
        }
        return services.get(port, "Unknown")

    def scan(self):
        """Perform the port scan"""
        if not self.target:
            raise ValueError("Target not set")
        
        if not self.ports:
            # Default to common ports if none specified
            self.add_port_range(1, 1000)
        
        print(f"Starting {self.scan_type.upper()} scan of {self.target}")
        print(f"Scanning {len(self.ports)} ports")
        print("-" * 50)
        
        start_time = datetime.now()
        
        # Limit concurrent threads
        semaphore = threading.Semaphore(self.max_threads)
        
        def thread_worker(port):
            semaphore.acquire()
            try:
                self.scan_port(port)
            finally:
                semaphore.release()
        
        # Create and start threads
        for port in self.ports:
            thread = threading.Thread(target=thread_worker, args=(port,))
            thread.start()
            self.threads.append(thread)
        
        # Wait for all threads to complete
        for thread in self.threads:
            thread.join()
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        # Display results
        print("\n" + "="*50)
        print("SCAN RESULTS")
        print("="*50)
        
        if self.open_ports:
            print(f"{'PORT':<10} {'STATE':<15} {'SERVICE'}")
            print("-"*50)
            for port, service in sorted(self.open_ports):
                state = "open" if self.scan_type=="tcp" else service.split("/")[0]
                srv = service if self.scan_type=="tcp" else service.split("/")[-1]
                print(f"{port:<10} {state:<15} {srv}")
        else:
            print("No open ports found")
        
        print("-"*50)
        print(f"Scan completed in {duration.total_seconds():.2f} seconds")

def main():
    parser = argparse.ArgumentParser(description="Pmap -like Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", help="Port range (e.g., 1-1000) or comma-separated list (e.g., 22,80,443)")
    parser.add_argument("-t", "--type", choices=["tcp", "udp"], default="tcp", help="Scan type (default: tcp)")
    parser.add_argument("--timeout", type=float, default=1.0, help="Socket timeout in seconds (default: 1.0)")
    parser.add_argument("--threads", type=int, default=1000, help="Max concurrent threads (default: 1000)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--version", action="version", version="Pmap  1.0")
   
    
    args = parser.parse_args()
    
    scanner = Pmap()
    scanner.set_target(args.target)
    scanner.set_scan_type(args.type)
    scanner.set_timeout(args.timeout)
    scanner.set_max_threads(args.threads)
    scanner.set_verbose(args.verbose)
    
    if args.ports:
        if "-" in args.ports:
            # Range format (e.g., 1-1000)
            try:
                start, end = map(int, args.ports.split("-"))
                scanner.add_port_range(start, end)
            except ValueError:
                print("Invalid port range format. Use START-END (e.g., 1-1000)")
                sys.exit(1)
        elif "," in args.ports:
            # List format (e.g., 22,80,443)
            try:
                ports = [int(p) for p in args.ports.split(",")]
                scanner.add_port_list(ports)
            except ValueError:
                print("Invalid port list format. Use comma-separated integers (e.g., 22,80,443)")
                sys.exit(1)
        else:
            # Single port
            try:
                scanner.add_port_list([int(args.ports)])
            except ValueError:
                print("Invalid port specification")
                sys.exit(1)
    
    try:
        scanner.scan()
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error during scan: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()