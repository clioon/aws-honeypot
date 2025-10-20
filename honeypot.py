import socket
import datetime
import requests
import os
from dotenv import load_dotenv
import banners

load_dotenv()

# =====================
HOST = '0.0.0.0'
PORT = 23 #Telnet
LOG_FILE = "honeypot_log.txt"
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
BANNER_NAME = os.getenv("BANNER_NAME", "telnet_ubuntu")
BANNER_TO_SEND = banners.BANNERS.get(BANNER_NAME, banners.BANNERS["default"])
# =====================

def get_geolocation(ip):
    try: 
        url = f"https://api.ipinfo.io/lite/{ip}?token={IPINFO_TOKEN}"
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
                # Connection start
                conn, addr = s.accept()
                with conn:
                    # Get IP location info
                    geo_info = get_geolocation(addr[0])
                    log_connection = f"[NEW CONNECTION]: IP: {addr[0]}:{addr[1]} | {geo_info}"
                    print(log_connection)
                    write_log(log_connection)

                    # Send fake banner
                    conn.sendall(BANNER_TO_SEND)

                    # Wait to capture response
                    conn.settimeout(10.0)

                    while True:
                        try:
                            recv_data = conn.recv(1024)
                            
                            if recv_data:
                                data_decode = recv_data.decode('utf-8', 'ignore').strip()
                                log_data = f"[RX] From {addr[0]}:{addr[1]} | Message: {data_decode}"
                                print(log_data)
                                write_log(log_data)
                            
                            else: 
                                log_closed = f"[CONNECTION CLOSED] clent {addr[0]}:{addr[1]} disconnected"
                                print(log_closed)
                                write_log(log_closed)
                                break

                        except socket.timeout:
                            log_timeout = f"[CONNECTION TIMEOUT] client {addr[0]}:{addr[1]} did not respond."
                            print(log_timeout)
                            write_log(log_timeout)
                            break

                        except Exception as e:
                            log_connError = f"[CONNECTION ERROR] connection with client {addr[0]}:{addr[1]} error"
                            print(log_connError)
                            write_log(log_connError)
                            break

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
