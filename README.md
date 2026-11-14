<img width="613" height="300" alt="Screenshot 2026-11-13 at 5 07 53 PM" src="https://github.com/user-attachments/assets/5a07cbaf-4a6f-4f34-b6ec-09d99496f67b" />


# Wireshark Lab: Finding a Plaintext Password in HTTP Traffic

#Goal: capture a login sent over HTTP and find the password in the packets, to show why unencrypted logins are unsafe.

Diagram comparing what Wireshark sees over HTTP and HTTPS

### Overview

When a website uses plain HTTP, everything the browser sends travels across the network as readable text, including usernames and passwords. Anyone who can capture that traffic can read it.

This lab proves that with a packet capture. I run a small practice login page on my own computer, sign in with fake credentials, and use Wireshark to pull the password straight out of the traffic.

### The four steps of the lab

### 1. Start the practice login page
bash
git clone https://github.com/YOUR-USERNAME/wireshark-plaintext-password.git
cd wireshark-plaintext-password
python3 login_server.py     # on Windows: python login_server.py

The page is served at http://127.0.0.1:8080. It does not store or check anything.

### 2. Capture on the loopback interface

Open Wireshark and double-click the loopback interface. Loopback carries traffic that stays inside your own computer.

System	Interface name
Windows	Adapter for loopback traffic capture
macOS	Loopback: lo0
Linux	Loopback: lo
### 3. Sign in with fake credentials

Open http://127.0.0.1:8080 in a browser, type a made-up username and password, and press Sign in. Then stop the capture with the red square in Wireshark.

###4. Filter for the POST and read it

Type this display filter and press Enter:

http.request.method == "POST"

Click the POST /login packet, then expand HTML Form URL Encoded in the details pane. The username and password are right there.

Diagram of the Wireshark panes and where the password appears

Shortcut: to skip the capture, open capture/sample-http-login.pcap in Wireshark and start at step 4. The credentials in that file are labuser / NotARealPassword123.

Results
<!-- Add your own screenshots to the screenshots/ folder. See screenshots/README.md for what to capture. -->

The filter narrows the capture down to the login request.

Packet list filtered to the POST request

The password is readable in the packet details.

Form items showing the username and password

Follow TCP Stream shows the whole request as the server received it.

TCP stream showing the full request

##Why this matters
HTTP has no encryption. The form data sits in the packet as plain text, so capturing the traffic is all it takes to read it.
The attacker does not need the server. Anyone on the path between the browser and the site can do this, for example on shared or public Wi-Fi.
Password reuse makes it worse. One exposed password often unlocks other accounts.
How to fix it
Fix	What it does
Serve the site over HTTPS	TLS encrypts the request, so a capture shows only unreadable Application Data
Redirect HTTP to HTTPS	Stops users from landing on the unencrypted version by accident
Turn on HSTS	Tells browsers to use HTTPS for the site every time
Mark cookies as Secure	Keeps session cookies from being sent over HTTP
Filters used
Filter	Shows
http	All HTTP traffic
http.request.method == "POST"	Form submissions
tcp.port == 8080	Everything to and from the practice page
frame contains "password"	Any packet containing the word "password"
Ethics

Only capture traffic on networks and devices you own or have written permission to test. This lab stays on the loopback interface, so no one else's traffic is involved, and it uses fake credentials only.

Author

Caleb Abreu
