import socket
import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

HOST = '0.0.0.0'
PORT = 23 #Telnet
LOG_FILE = "honeypot_log.txt"
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")

def get_geolocation(ip):
    try: 
        url = f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        name = data.get("as_name", "Unknown")
        domain = data.get("as_domain", "Unknown")
        country = data.get("country", "Unknown")
        continent = data.get("continent", "Unknown")

        return f"Name: {name} | Domain: {domain} | Country: {country} | Continent: {continent}"
    
    except requests.exceptions.RequestException as e:
        return f"Unable to get ip location: {e}"

def write_log(message):    
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #UTC 0
        f.write(f"[{timestamp}] {message}\n")

def start_honeypot(host, port):
    print(f"[*] Honeypot started on port {port}...")
    write_log(f"Honeypot started: {host}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        while True:
            try:
                conn, addr = s.accept()
                with conn:
                    geo_info = get_geolocation(addr[0])
                    log_message = f"[NEW CONNECTION]: IP: {addr[0]}:{addr[1]} | {geo_info}"
                    print(log_message)
                    write_log(log_message)
                    conn.sendall(b"Welcome to the Telnet server!\r\nUsername: ")
            except Exception as e:
                error_message = f"Error: {e}"
                print(f"[!] {error_message}")
                write_log(error_message)

if __name__ == "__main__":
    try:
        start_honeypot(HOST, PORT)
    except KeyboardInterrupt:
        print("\n[*] Closing honeypot.")
        write_log("Honeypot successfully closed.")
    except Exception as e:
        critical_error = f"Honeypot starting error: {e}"
        print(f"[!!] {critical_error}")
        write_log(critical_error)
