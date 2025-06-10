# 🛡️ ReconX — Web-Based Network Reconnaissance Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange.svg)
![License](https://img.shields.io/badge/License-BSD%203--Clause-green.svg)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

![ReconX Banner](https://your-image-link.com/banner.png)

---

## 📌 Overview

**ReconX** is a powerful, all-in-one **network security reconnaissance toolkit** built with a modern **Streamlit web interface**. Designed for **penetration testers, ethical hackers, red teamers**, and **cybersecurity enthusiasts**, ReconX brings together essential active and passive recon techniques in one lightweight, interactive dashboard.

Whether you’re prepping for a CTF, conducting OSINT, scanning your own infrastructure, or just learning the ropes, **ReconX empowers you to explore and assess digital footprints — securely, silently, and effectively**.

🔗 **Live Demo**: [ReconX Web App](https://reconx.streamlit.app/)  
📂 **Source Code**: [ReconX GitHub](https://github.com/atharvbyadav/ReconX)

---

## 🚀 Features

### 1️⃣ Port Scanning
- Multithreaded TCP port scanner (range: 1–500)
- Detects open ports, grabs banners, highlights outdated services

### 2️⃣ OS Fingerprinting
- Basic TCP handshake analysis to infer Linux/Unix vs Windows OS

### 3️⃣ WHOIS Lookup
- Retrieves domain ownership and registrar information

### 4️⃣ Reverse DNS Lookup
- Resolves IPs back to domain names (if records exist)

### 5️⃣ DNS Enumeration
- Retrieves A, AAAA, MX, NS, CNAME, TXT records for a domain

### 6️⃣ GhostPath (Passive Recon)
- Extracts subdomains via `crt.sh`
- Gathers archived URLs via the Wayback Machine
- Fully passive — no requests to target servers

---

## 🧠 Under the Hood

**ReconX** may look like a polished web app — and it is — but under the hood, it’s powered by a well-organized collection of recon logic packed efficiently into a single, maintainable Python script.

Instead of scattering logic across multiple files or scripts, all core functionalities — **Port Scanning**, **OS Fingerprinting**, **WHOIS Lookup**, **DNS Enumeration**, **Reverse DNS**, and **GhostPath** — are implemented as **individual Python classes within one main file**.

This approach provides:
- A clean, modular structure without file sprawl
- Easier debugging — you only focus on the relevant class
- Smooth onboarding for contributors or learners

---

### 🌐 Streamlit-Powered UI

The app’s interface is built with **Streamlit**, enabling a fast, reactive, and browser-based frontend. Each recon class is wrapped in Streamlit UI components:
- Text inputs for target domains/IPs
- Buttons to trigger scans
- Sections with expanders, tables, and logs to display results

---

### 👻 Integrated GhostPath Engine

ReconX also embeds **GhostPath**, a passive reconnaissance engine that runs directly in the app. It consists of two internal classes:
- `GhostSubdomains`: Fetches subdomains using **crt.sh**
- `GhostWayback`: Gathers archived URLs from the **Wayback Machine**

These components operate quietly in the background, leaving no footprint on the target. They're perfect for stealthy reconnaissance workflows and OSINT-based enumeration.

---

### 🚀 Why This Architecture Works

- ✅ **All-in-one file** means simpler code navigation and faster debugging  
- ✅ **Class-based design** provides modularity and clarity  
- ✅ **Streamlit frontend** offers interactivity without extra complexity  
- ✅ **GhostPath integration** brings passive recon into your active workflow  

---

## 🛠️ Installation & Usage

### Prerequisites
Ensure you have **Python 3.x** installed.

### Clone the Repository
```bash
git clone https://github.com/atharvbyadav/ReconX.git
cd ReconX
````

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch the App

```bash
streamlit run ReconX.py
```

---

## 📖 Usage Guide

### 🔸 Port Scanning

Enter the **Target IP**, hit **Scan**, and see open ports, banners, and potential risks.

### 🔸 OS Fingerprinting

Enter an IP and run detection to infer the OS type.

### 🔸 WHOIS Lookup

Enter a domain or IP to view WHOIS data.

### 🔸 Reverse DNS Lookup

Reverse resolve an IP to any registered domain.

### 🔸 DNS Enumeration

Enter a domain name to pull DNS records.

### 🔸 GhostPath (Passive Recon)

Use **crt.sh** and **Wayback Machine** to uncover historical data and subdomains.

---

## ⚠️ Disclaimer

This tool is for **educational and authorized security research purposes only**. Scanning networks you don't own or lack permission to test is **illegal**.

Use responsibly. Stay ethical.

---

## 📜 License

This project is licensed under the **BSD 3-Clause License**.
See the [LICENSE](LICENSE) file for full details.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to **fork this repo**, improve or expand features, and open a **pull request**.

Have ideas? Open an issue or reach out via the contact links below.

---

## 📬 Contact

**👨‍💻 Author**: Atharv Yadav
**🌐 Website**: [atharvbyadav.github.io](https://atharvbyadav.github.io)
**🐙 GitHub**: [@atharvbyadav](https://github.com/atharvbyadav)
**🧠 LinkedIn**: [Atharv Yadav](https://www.linkedin.com/in/atharvbyadav/)
**💬 Twitter/X**: [@AtharvYadavB](https://x.com/AtharvYadavB)

> *"Collaboration is the backbone of innovation. Let’s build better tools together."*

---
