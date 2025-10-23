A powerful, feature-rich port scanner built with Python that provides Nmap-like functionality with enhanced capabilities for network reconnaissance and security assessment.

Features ✨
🚀 Multi-threaded Scanning - Fast concurrent port scanning

🎯 Multiple Target Support - Scan single IP, multiple IPs, or entire network ranges

🔍 TCP & UDP Scanning - Comprehensive protocol support

📊 Banner Grabbing - Service version detection

💻 OS Detection - Basic OS fingerprinting using TTL analysis

📁 File I/O - Save results and load targets from files

📈 Progress Tracking - Real-time progress bar for long scans

🔧 Customizable Settings - Adjustable timeout, threads, and scan parameters

🎨 Verbose Output - Detailed scanning information

Installation 🛠️
Prerequisites
Python 3.6 or higher

No external dependencies required

Download & Run
bash
# Clone or download the script
git clone <repository-url>
cd advanced-port-scanner

# Run directly
python advanced_scanner.py --help
Quick Start 🚀
Basic Scan
bash
python advanced_scanner.py 192.168.1.1
Common Ports Scan
bash
python advanced_scanner.py example.com -p 22,80,443,8080
Comprehensive Scan
bash
python advanced_scanner.py 192.168.1.1 -p 1-1000 --banner --os-scan --progress
Usage Examples 📝
Network Discovery
bash
# Scan entire subnet
python advanced_scanner.py --network 192.168.1.0/24 -p 22,80,443

# Scan multiple targets from file
python advanced_scanner.py -i targets.txt -p 1-100
Service Detection
bash
# Banner grabbing on common services
python advanced_scanner.py 192.168.1.1 -p 21,22,23,25,80,110,443 --banner

# OS detection with verbose output
python advanced_scanner.py 192.168.1.1 --os-scan -v
Performance Scanning
bash
# Fast scan with custom settings
python advanced_scanner.py 192.168.1.1 -p 1-1000 --threads 500 --timeout 0.3

# UDP scanning
python advanced_scanner.py 192.168.1.1 -t udp -p 53,67,68,161
Reporting
bash
# Save results to file
python advanced_scanner.py 192.168.1.1 -p 1-1000 -o scan_results.txt

# Comprehensive scan with all features
python advanced_scanner.py 192.168.1.1 -p 1-65535 --banner --os-scan --progress -o full_scan.txt --threads 1000
Command Line Options ⚙️
Basic Options
Option	Description	Default
target	Target IP/hostname	Required
-p, --ports	Ports to scan (1-1000 or 22,80,443)	1-1000
-t, --type	Scan type: tcp/udp	tcp
--timeout	Socket timeout (seconds)	1.0
--threads	Maximum concurrent threads	1000
-v, --verbose	Enable verbose output	False
Advanced Features
Option	Description
--banner	Enable banner grabbing
--os-scan	Enable OS detection
-o, --output	Save results to file
--progress	Show progress bar
-i, --input-file	Read targets from file
--network	Scan network range (CIDR)
Output Examples 📊
Sample Scan Output
text
Starting TCP scan of 192.168.1.1
OS detection: Windows
Scanning 100 ports
--------------------------------------------------
Progress: |████████████████████████████████████████| 100.0%

==================================================
SCAN RESULTS - 192.168.1.1
==================================================
PORT      STATE           SERVICE             BANNER
22        open            SSH                 SSH-2.0-OpenSSH_8.2
80        open            HTTP                HTTP/1.1 200 OK...
443       open            HTTPS               HTTP/1.1 200 OK...
--------------------------------------------------
Scan completed in 5.23 seconds
File Output Format
text
Scan results for 192.168.1.1
==================================================
Scan type: TCP
Scan time: 2024-01-15 10:30:45

PORT      STATE           SERVICE             BANNER
22        open            SSH                 SSH-2.0-OpenSSH_8.2
80        open            HTTP                HTTP/1.1 200 OK...
443       open            HTTPS               HTTP/1.1 200 OK...

==================================================
Service Detection 🛰️
The scanner automatically detects common services including:

Web Services: HTTP (80), HTTPS (443), HTTP-Alt (8080, 8443)

Remote Access: SSH (22), Telnet (23), RDP (3389), VNC (5900)

Email Services: SMTP (25), POP3 (110), IMAP (143)

File Transfer: FTP (21), TFTP (69)

Database: MySQL (3306), PostgreSQL (5432), MSSQL (1433)

Network Services: DNS (53), DHCP (67,68), SNMP (161)

Performance Tuning ⚡
Optimizing Scan Speed
bash
# Fast scan (responsive networks)
python advanced_scanner.py target --timeout 0.3 --threads 1000

# Reliable scan (high-latency networks)
python advanced_scanner.py target --timeout 2.0 --threads 100
Resource Management
bash
# Low resource usage
python advanced_scanner.py target --threads 50

# Maximum performance
python advanced_scanner.py target --threads 2000
Advanced Usage 🧩
Creating Target Files
bash
# targets.txt
192.168.1.1
192.168.1.10
192.168.1.15-192.168.1.20
example.com
Batch Scanning
bash
# Scan multiple subnets
for subnet in 192.168.1.0/24 192.168.2.0/24; do
    python advanced_scanner.py --network $subnet -p 22,80,443 -o scan_$subnet.txt
done
Integration with Other Tools
bash
# Pipe results to grep
python advanced_scanner.py 192.168.1.1 -p 1-1000 | grep "open"

# Save open ports to file
python advanced_scanner.py 192.168.1.1 -p 1-1000 -o results.txt && cat results.txt | grep "open" > open_ports.txt
Limitations ⚠️
UDP Reliability: UDP scanning may be less reliable than TCP

OS Detection: Basic TTL-based detection, not as accurate as advanced fingerprinting

Firewall Evasion: No built-in stealth or evasion techniques

Privilege Requirements: Some features may require elevated privileges

Service Detection: Limited to common port-service mappings

Legal Disclaimer ⚖️
This tool is intended for:

✅ Educational purposes

✅ Security research with proper authorization

✅ Network administration on owned systems

✅ Penetration testing with explicit permission

⚠️ Important: Unauthorized scanning of networks and systems may be:

Illegal in your jurisdiction

Against terms of service

Considered hostile activity

Always obtain proper authorization before scanning any network or system you don't own.

Troubleshooting 🔧
Common Issues
Slow Scanning: Increase --threads or decrease --timeout

No Results: Check target connectivity and firewall settings

Permission Errors: Run with appropriate privileges

Memory Issues: Reduce --threads value

Debug Mode
bash
python advanced_scanner.py target -v --timeout 5
Version History 📚
v2.0 (Current): Advanced features, multiple targets, banner grabbing

v1.0: Basic TCP/UDP port scanning functionality

Contributing 🤝
Contributions are welcome! Please feel free to submit pull requests or open issues for:

Bug fixes

New features

Performance improvements

Documentation updates

License 📄
This project is intended for educational and authorized security testing purposes. Use responsibly and ethically.

Happy Scanning! 🎯

For questions or issues, please open a GitHub issue or contact the development team.

Pmap version 1.1
