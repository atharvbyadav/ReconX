# 🛡️ ReconX Scan — Network Security Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange.svg)
![License](https://img.shields.io/badge/License-BSD%203--Clause-green.svg)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 📌 Overview

**ReconX Scan** is your **all-in-one network reconnaissance and analysis toolkit**, designed for **penetration testers, ethical hackers, red teamers**, and **cybersecurity enthusiasts**.

Built with **Streamlit**, ReconX offers a modern web-based interface for carrying out essential reconnaissance tasks that are typically scattered across multiple tools. From scanning ports and fingerprinting operating systems to performing detailed DNS enumeration and WHOIS lookups, this tool empowers users to perform passive and active recon with minimal setup and no steep learning curve.

> Whether you're auditing your infrastructure, preparing for a Capture The Flag (CTF), or conducting open-source intelligence gathering (OSINT), **ReconX** simplifies your recon workflow — responsibly and effectively.

🔗 **Live Demo**: [ReconX Web App](https://reconx.streamlit.app/)

📂 **Repository**: [ReconX GitHub](https://github.com/atharvbyadav/ReconX)

---

## ✍️ Author

Created by **Atharv Yadav** — [GitHub Profile](https://github.com/atharvbyadav)

---

## 🚀 Features

### 1️⃣ **Port Scanning**
- Scans a given target IP within the range **1-500**.
- Uses **multi-threading (50 threads)** to speed up scanning.
- Detects **open ports, service banners**, and **potential vulnerabilities**.
- Identifies **outdated services** that may have known exploits.

### 2️⃣ **OS Fingerprinting**
- Uses a **basic TCP handshake technique** to infer the target OS.
- Determines if the system is **Linux/Unix or Windows Server** based on response analysis.

### 3️⃣ **Whois Lookup**
- Fetches **WHOIS information** for a given domain or IP.
- Useful for gathering ownership details and domain registration data.

### 4️⃣ **Reverse DNS Lookup**
- Converts an **IP address to a domain name** (if available).
- Helps in identifying associated domains with an IP.

### 5️⃣ **DNS Enumeration**
- Retrieves important **DNS records (A, AAAA, MX, NS, CNAME, TXT)**.
- Helps in subdomain enumeration and understanding domain infrastructure.

---

## 🧠 Theory Behind The Features

### 🔹 Port Scanning
Port scanning is an **active reconnaissance technique** used to identify open ports on a target machine. Open ports can indicate running services, which may be exploitable.

### 🔹 OS Fingerprinting
By analyzing responses to network requests, we can make an educated guess about the OS running on the target.

### 🔹 Whois Lookup
WHOIS databases store **domain ownership information**. Retrieving this data helps in reconnaissance by providing details about registrants, contact info, and hosting providers.

### 🔹 Reverse DNS Lookup
Maps an IP address back to a domain name. If a reverse DNS record exists, it provides clues about the target.

### 🔹 DNS Enumeration
DNS records contain valuable information about a domain’s infrastructure, such as mail servers (MX), authoritative name servers (NS), and textual metadata (TXT).

---

## 🛠️ Installation & Usage

### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Step 1️⃣ - Clone the Repository
```sh
git clone https://github.com/atharvbyadav/ReconX.git
cd ReconX

Step 2️⃣ - Install Dependencies

pip install -r requirements.txt

Step 3️⃣ - Run the Application

streamlit run ReconX.py

The application will open in your default web browser.


---

📖 Usage Guide

🔸 Port Scanning

1. Enter the Target IP Address.


2. Click Start Port Scan.


3. View the open ports, banners, outdated services, and potential risks.



🔸 OS Fingerprinting

1. Enter the Target IP Address.


2. Click Detect OS.


3. View the estimated OS of the target.



🔸 Whois Lookup

1. Enter the Domain or IP Address.


2. Click Get WHOIS Info.


3. View the WHOIS data fetched from public databases.



🔸 Reverse DNS Lookup

1. Enter the Target IP Address.


2. Click Perform Reverse DNS Lookup.


3. View the associated domain (if any).



🔸 DNS Enumeration

1. Enter the Domain Name.


2. Click Enumerate DNS.


3. View all DNS records found.




---

⚠️ Disclaimer

This tool is meant for educational and security research purposes only. Unauthorized scanning of networks you do not own or have explicit permission to test is illegal and punishable under cyber laws.

Use this tool responsibly and ethically!


---

🤝 Contributing

We welcome contributions! Feel free to fork this repository, improve the tool, and submit a pull request.

Reach out for ideas and suggestions...


---

📜 License

This project is licensed under the BSD 3-Clause License.


---

📬 Contact Me

If you have any questions, feedback, or collaboration ideas, feel free to reach out:

🔗 GitHub: @atharvbyadav

🌐 Portfolio: atharvbyadav.github.io