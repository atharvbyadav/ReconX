import streamlit as st
import socket
import threading
import queue
import pandas as pd
import whois
import dns.resolver
import dns.reversename
import io

# Streamlit page config
st.set_page_config(page_title="NetSec Scanner", layout="wide")

# Sidebar Setup
st.sidebar.title("🔍 Network Security Toolkit")
st.sidebar.write("Navigate:")
selected_tab = st.sidebar.radio("Select a feature:", ["Port Scanning", "OS Fingerprinting", "Whois Lookup", "Reverse DNS Lookup", "DNS Enumeration"], index=0)

# Number of threads for parallel scanning
THREAD_COUNT = 50
PORT_RANGE = range(1, 500)
port_queue = queue.Queue()
scan_results = []
vulnerable_ports = []
os_guess = "Unknown"

# Common vulnerable services
VULNERABLE_SERVICES = {
    21: {"name": "FTP", "risk": "Potential Anonymous Login"},
    22: {"name": "SSH", "risk": "Check for Weak Credentials"},
    23: {"name": "Telnet", "risk": "Insecure, Avoid Usage"},
    25: {"name": "SMTP", "risk": "Open Relay Misconfiguration?"},
    80: {"name": "HTTP", "risk": "Check for Misconfigurations"},
    110: {"name": "POP3", "risk": "Older Versions May Be Exploitable"},
    3306: {"name": "MySQL", "risk": "Check for Default Credentials"},
}

def detect_os(ip):
    global os_guess
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, 80))
        s.send(b'\x16\x03\x01')
        response = s.recv(1024)
        s.close()
        if response:
            os_guess = "Linux/Unix or Windows Server"
        else:
            os_guess = "Unknown"
        return os_guess
    except:
        return "Unknown"

def check_open_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        s.close()
        return result == 0
    except:
        return False

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024).decode("utf-8", errors="ignore").strip()
        s.close()
        return banner if banner else "No Banner"
    except:
        return "No Banner"

def detect_outdated_services(banner):
    outdated_keywords = ["OpenSSL 1.0", "Apache 2.2", "PHP 5.", "vsftpd 2.3.4"]
    for keyword in outdated_keywords:
        if keyword in banner:
            return f"Outdated Service Detected: {keyword}"
    return "Up-to-date"

def scan_target(ip):
    while not port_queue.empty():
        port = port_queue.get()
        if check_open_port(ip, port):
            banner = grab_banner(ip, port)
            outdated_status = detect_outdated_services(banner)
            service_info = VULNERABLE_SERVICES.get(port, {"name": "Unknown", "risk": "None"})
            scan_results.append([port, service_info["name"], banner, outdated_status, service_info["risk"]])
            if service_info["risk"] != "None" or "Outdated Service" in outdated_status:
                vulnerable_ports.append([port, service_info["name"], outdated_status, service_info["risk"]])
        port_queue.task_done()

def whois_lookup(target):
    try:
        result = whois.whois(target)
        return result.text
    except Exception as e:
        return f"Error fetching WHOIS data: {str(e)}"

def reverse_dns_lookup(ip):
    try:
        rev_name = dns.reversename.from_address(ip)
        return str(dns.resolver.resolve(rev_name, "PTR")[0])
    except:
        return "No Reverse DNS Found"

def dns_enumeration(domain):
    records = {}
    record_types = ["A", "AAAA", "MX", "NS", "CNAME", "TXT"]
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            records[record] = [str(rdata) for rdata in answers]
        except:
            records[record] = "No Record Found"
    return records

def main():
    st.title("🔍 NetSec - Network Security Toolkit")

    if selected_tab == "Port Scanning":
        st.header("Port Scanning")
        ip = st.text_input("Enter Target IP for Port Scan:", "192.168.1.1")
        if st.button("Start Port Scan"):
            scan_results.clear()
            vulnerable_ports.clear()
            for port in PORT_RANGE:
                port_queue.put(port)
            threads = [threading.Thread(target=scan_target, args=(ip,)) for _ in range(THREAD_COUNT)]
            for thread in threads:
                thread.daemon = True
                thread.start()
            port_queue.join()
            df = pd.DataFrame(scan_results, columns=["Port", "Service", "Banner", "Outdated Status", "Potential Risk"])
            st.dataframe(df)
            if vulnerable_ports:
                st.write("### ⚠️ Potentially Vulnerable Services Found")
                df_vuln = pd.DataFrame(vulnerable_ports, columns=["Port", "Service", "Outdated Status", "Risk"])
                st.dataframe(df_vuln)
            st.success("Port Scan Complete!")

    elif selected_tab == "OS Fingerprinting":
        st.header("OS Fingerprinting")
        ip = st.text_input("Enter Target IP for OS Fingerprinting:", "192.168.1.1")
        if st.button("Detect OS"):
            os_guess = detect_os(ip)
            st.write(f"### OS Detected: {os_guess}")
            st.success("OS Fingerprinting Complete!")

    elif selected_tab == "Whois Lookup":
        st.header("Whois Lookup")
        target = st.text_input("Enter Domain or IP for WHOIS Lookup:", "example.com")
        if st.button("Get WHOIS Info"):
            whois_data = whois_lookup(target)
            st.text_area("WHOIS Information:", whois_data, height=300)
            st.success("WHOIS Lookup Complete!")

    elif selected_tab == "Reverse DNS Lookup":
        st.header("Reverse DNS Lookup")
        ip = st.text_input("Enter IP Address:", "8.8.8.8")
        if st.button("Perform Reverse DNS Lookup"):
            result = reverse_dns_lookup(ip)
            st.write(f"**Reverse DNS Result:** {result}")

    if selected_tab == "DNS Enumeration":
        st.header("DNS Enumeration")
        domain = st.text_input("Enter Domain:", "example.com")
        if st.button("Enumerate DNS"):
            results = dns_enumeration(domain)
            for key, value in results.items():
                with st.expander(f"### {key} Records"):
                    if isinstance(value, list):
                        for item in value:
                            st.write(f"- {item}")
                    else:
                        st.write(f"- {value}")

if __name__ == "__main__":
    main()