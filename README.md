# Internal HTTP Credential Capture Demo

## Overview
This project demonstrates how plaintext credentials can be intercepted when an application uses HTTP instead of HTTPS. A simple Python-based login page is hosted locally, test credentials are submitted, and the traffic is inspected to reveal sensitive data in cleartext.

The purpose of this project is to highlight the risks of unencrypted HTTP traffic and to demonstrate practical traffic inspection techniques in a Linux environment.

---

## Environment
- **Victim System:** ChromeOS device running Linux (Crostini)
- **Analyst System:** Linux laptop (Dell)
- **Web Server:** Python 3 HTTP server
- **Traffic Analysis Tool:** `tcpdump`
- **Protocol:** HTTP (intentionally unencrypted)

> Note: ChromeOS Crostini restricts low-level packet capture via Wireshark/dumpcap. Due to these platform limitations, `tcpdump` was used to inspect loopback traffic within the Linux container.

---

## Project Architecture

[ Browser ]
|
| HTTP POST (credentials)
v
[ Python Web Server :8080 ]
|
v
[ tcpdump (loopback capture) ]

All traffic occurs locally within the Linux container, allowing credential exposure to be observed without external network sniffing.

---

## Methodology

1. A Python HTTP server hosts a login form on port `8080`
2. Test credentials are submitted through the browser
3. `tcpdump` captures HTTP traffic on the loopback interface
4. Submitted credentials are observed in plaintext within the packet payload

---

## Evidence

Screenshots included in this repository demonstrate:
- The HTTP server running locally
- Credential submission via the browser
- Captured HTTP POST request revealing credentials in cleartext

See the `screenshots/` directory for supporting evidence.

---

## Key Takeaways
- HTTP transmits credentials in plaintext
- Any local attacker with packet capture access can read sensitive data
- HTTPS is mandatory for protecting authentication data
- Platform restrictions may require adapting tooling (e.g., tcpdump vs Wireshark)

---

## Disclaimer
All testing was performed in a controlled environment using test credentials on systems owned by the author. No unauthorized interception or real user data was involved.
