# Pmap
Pmap is a tool for scaning ip addreses and port of  webpage 
A lightweight, multi-threaded port scanner built with Python that mimics some of the basic functionality of Nmap.

Features
🚀 Fast Multi-threaded Scanning - Scan thousands of ports concurrently

🔍 Multiple Scan Types - TCP connect scanning and basic UDP scanning

🎯 Flexible Port Targeting - Scan specific ports, ranges, or use common ports

📊 Service Detection - Automatically detects common services on open ports

💬 Verbose Output - Real-time scanning progress with detailed information

⚡ Customizable Settings - Adjustable timeout and thread limits

Installation
Prerequisites
Python 3.6 or higher

No external dependencies required

Download
bash
git clone <repository-url>
cd pmap
Usage
Basic Syntax
bash
python pmap.py TARGET [OPTIONS]
Command Line Options
Option	Description	Default
-p, --ports	Port range (1-1000) or comma-separated list (22,80,443)	1-1000
-t, --type	Scan type: tcp or udp	tcp
--timeout	Socket timeout in seconds	1.0
--threads	Maximum concurrent threads	1000
-v, --verbose	Enable verbose output	False
--version	Show version information	-
Examples
Basic TCP Scan
bash
# Scan common ports on a target
python Pmap.py 192.168.1.1

# Scan specific host with default settings
python Pmap.py example.com
Specific Port Scans
bash
# Scan a port range
python pmap.py 192.168.1.1 -p 1-1000

# Scan specific ports
python pmap.py 192.168.1.1 -p 22,80,443,8080

# Scan single port
python pmap.py 192.168.1.1 -p 80
UDP Scanning
bash
# UDP scan on common ports
python Pmap.py 192.168.1.1 -t udp

# UDP scan on specific ports
python Pmap.py 192.168.1.1 -t udp -p 53,67,68,161
Advanced Options
bash
# Faster scan with reduced timeout
python Pmap.py 192.168.1.1 --timeout 0.5 -p 1-1000

# Limited threads for resource-constrained environments
python Pmap.py 192.168.1.1 --threads 100 -p 1-500

# Verbose output to see real-time progress
python Pmap.py 192.168.1.1 -v -p 20-100
Comprehensive Scan
bash
# Full scan with verbose output and custom settings
python Pmap.py 192.168.1.1 -t tcp -p 1-65535 --threads 500 --timeout 0.3 -v
Output Example
text
Starting TCP scan of 192.168.1.1
Scanning 100 ports
--------------------------------------------------

Port 22 is open (SSH)
Port 80 is open (HTTP)
Port 443 is open (HTTPS)

==================================================
SCAN RESULTS
==================================================
PORT        STATE           SERVICE
22          open            SSH
80          open            HTTP
443         open            HTTPS
--------------------------------------------------
Scan completed in 12.34 seconds
Service Detection
The tool automatically detects common services including:

SSH (22), HTTP (80), HTTPS (443)

FTP (21), DNS (53), SMTP (25)

RDP (3389), MySQL (3306), PostgreSQL (5432)

And many more...

Performance Tips
Timeout Settings: Lower timeout values (0.3-0.5) for faster scans on responsive networks

Thread Count: Increase threads for faster scanning (be mindful of system resources)

Port Selection: Target specific ports instead of full ranges for quicker results

Network Conditions: Adjust settings based on network latency and target responsiveness

Limitations
UDP scanning is basic and may not be as reliable as specialized tools

Service detection is based on common port assignments

No OS detection or advanced fingerprinting

Limited error handling for complex network scenarios

Legal Disclaimer
This tool is intended for:

Educational purposes

Security research with proper authorization

Network administration on owned systems

Security assessment with explicit permission

⚠️ Warning: Unauthorized port scanning may be illegal in your jurisdiction. Always obtain proper authorization before scanning any network or system you don't own.

Version
Pmap 1.0

Contributing
Feel free to submit issues and enhancement requests!

License
This project is for educational purposes. Use responsibly and ethically.


