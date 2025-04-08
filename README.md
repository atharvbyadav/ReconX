# ReconX Scan - Network Security Toolkit 🔍

## Table of Contents 📑
1. [Overview](#overview-)
2. [Author](#author-)
3. [Features](#features-)
4. [Theory Behind The Features](#theory-behind-the-features-)
5. [Installation & Usage](#installation--usage-)
6. [Usage Guide](#usage-guide-)
7. [Disclaimer](#disclaimer-)
8. [Contributing](#contributing-)
9. [License](#license-)

---

## Overview 📌
**ReconX Scan** is an advanced **network security toolkit** built with **Streamlit** that provides a user-friendly interface for cybersecurity tasks. This tool helps security analysts, penetration testers, and IT professionals perform essential network reconnaissance and security assessments.

🚀 **Live Demo**: [ReconX](https://reconx.streamlit.app/)

## Author ✍️
Created by **Atharv Yadav** - [GitHub Profile](https://github.com/atharvbyadav)

🔗GitHub Repository: [ReconX](https://github.com/atharvbyadav/ReconX)

## Features 🚀
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
## Theory Behind The Features 🧠
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
## Installation & Usage 🛠️

### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Step 1️⃣ - Clone the Repository
```sh
git clone https://github.com/atharvbyadav/ReconX.git
cd ReconX
```

### Step 2️⃣ - Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3️⃣ - Run the Application
```sh
streamlit run ReconX.py
```

The application will open in your default web browser.

---
## Usage Guide 📖

### 🔸 **Port Scanning**
1. Enter the **Target IP Address**.
2. Click **Start Port Scan**.
3. View the open ports, banners, outdated services, and potential risks.

### 🔸 **OS Fingerprinting**
1. Enter the **Target IP Address**.
2. Click **Detect OS**.
3. View the estimated OS of the target.

### 🔸 **Whois Lookup**
1. Enter the **Domain or IP Address**.
2. Click **Get WHOIS Info**.
3. View the WHOIS data fetched from public databases.

### 🔸 **Reverse DNS Lookup**
1. Enter the **Target IP Address**.
2. Click **Perform Reverse DNS Lookup**.
3. View the associated domain (if any).

### 🔸 **DNS Enumeration**
1. Enter the **Domain Name**.
2. Click **Enumerate DNS**.
3. View all DNS records found.

---
## Disclaimer ⚠️
This tool is meant for **educational and security research purposes only**. Unauthorized scanning of networks you do not own or have explicit permission to test **is illegal** and punishable under cyber laws.

Use this tool **responsibly and ethically**!

---
## Contributing 🤝
We welcome contributions! Feel free to **fork this repository**, improve the tool, and submit a **pull request**.

---
## License 📜
This project is licensed under the **MIT License**.

