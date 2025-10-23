import socket
import datetime
import requests
import os
from dotenv import load_dotenv
import threading
import banners

load_dotenv()

# =====================
HOST = '0.0.0.0'
LOG_DIR = "logs"
MAIN_LOG_FILE = os.path.join(LOG_DIR, "honeypot_main.log")
LOG_LOCK = threading.Lock()
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
PORT_BANNER_MAP = {
    #21: "ftp_vsftpd",
    23: "telnet_ubuntu",
}
MAX_NUMBER_MESSAGES =  int(os.getenv("MAX_NUMBER_MESSAGES", "20"))
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

def write_log(message, filename):
    with LOG_LOCK:    
        with open(filename, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #UTC 0
            f.write(f"[{timestamp}] {message}\n")

def handle_connection(conn, addr, log_file):
    client_ip, client_port = addr
    my_port = conn.getsockname()[1]
    session_state = "LOGIN"

    try:
        # get ip loctaion info
        geo_info = get_geolocation(client_ip)
        log_connection = f"[NEW CONNECTION]: Port: {my_port} IP: {addr[0]}:{addr[1]} | {geo_info}"
        print(log_connection)
        write_log(log_connection, log_file)

        # banner
        banner_name = PORT_BANNER_MAP.get(my_port, "default")
        banner_profile = banners.BANNERS.get(banner_name, banners.BANNERS["default"])

        banner_to_send = banner_profile.get("initial", b"login: ")
        banner_success = banner_profile.get("success", b"\r\nWelcome\r\n")
        fake_prompt = banner_profile.get("prompt", b"# ")

        conn.sendall(banner_to_send)
        message_count = 0

        # interaction
        conn.settimeout(30.0)
        while True:
            if message_count >= MAX_NUMBER_MESSAGES:
                log_message_limit = f"[MESSAGE LIMIT] client {addr[0]}:{addr[1]} already sent {MAX_NUMBER_MESSAGES} messages."
                print(log_message_limit)
                write_log(log_message_limit, log_file)
                break

            try:
                recv_data = conn.recv(1024)

                if recv_data:
                    message_count += 1
                    data_decode = recv_data.decode('utf-8', 'ignore').strip()

                    if not data_decode: continue

                    if session_state == "LOGIN":
                        log_data = f"[LOGIN ATTEMPT] From {addr[0]}:{addr[1]} | User: {data_decode}"
                        print(log_data)
                        write_log(log_data, log_file)

                        if data_decode.lower() in ['root', 'admin', 'user', 'test', 'oracle']:
                            conn.sendall(b"Password: ")
                            session_state = "PASSWORD"
                        else:
                            conn.sendall(b"Incorrect login\r\n")
                            conn.sendall(banner_to_send)
                    
                    elif session_state == "PASSWORD":
                        log_data = f"[PASSWORD ATTEMPT] From {addr[0]}:{addr[1]} | Password: {data_decode}"
                        print(log_data)
                        write_log(log_data, log_file)

                        conn.sendall(banner_success)                        
                        conn.sendall(fake_prompt)
                        session_state = "SHELL"
                    
                    elif session_state == "SHELL":
                        log_data = f"[SHELL COMMAND] From {addr[0]}:{addr[1]} | Command: {data_decode}"
                        print(log_data)
                        write_log(log_data, log_file)

                        conn.sendall(f"bash: {data_decode}: command not found\r\n".encode('utf-8'))
                        conn.sendall(fake_prompt)
                
                else: 
                    log_closed = f"[CONNECTION CLOSED] clent {addr[0]}:{addr[1]} disconnected"
                    print(log_closed)
                    write_log(log_closed, log_file)
                    break

            except socket.timeout:
                log_timeout = f"[CONNECTION TIMEOUT] client {addr[0]}:{addr[1]} did not respond."
                print(log_timeout)
                write_log(log_timeout, log_file)
                break

            except Exception as e:
                log_connError = f"[CONNECTION ERROR] connection with client {addr[0]}:{addr[1]} error"
                print(f"{log_connError} : {e}")
                write_log(log_connError, log_file)
                break
    
    except Exception as e:
                error_message = f"Error: {e}"
                print(f"[!] {error_message}")
                write_log(error_message, log_file)

def start_listener(host, port):
    log_file = os.path.join(LOG_DIR, f"honeypot_port_{port}.log")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen()
            print(f"[*] 'Listener started. Listening on port {port}...")
            write_log(f"Listener started on port {port}", log_file)

            while True:
                conn, addr = s.accept()

                client_thread = threading.Thread(target=handle_connection, args=(conn, addr, log_file))
                client_thread.daemon = True
                client_thread.start()

    except Exception as e:
        error_message = f"Fatal error on port {port}: {e}"
        print(f"[!!] {error_message}")
        write_log(error_message, MAIN_LOG_FILE)

if __name__ == "__main__":
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
    except OSError as e:
        print(f"[!!] Error creating log directory '{LOG_DIR}': {e}")
        exit()

    print("[*] 'Starting honeypot...")
    write_log("[*] Starting honeypot...", MAIN_LOG_FILE)
    
    listener_threads = []

    for port in PORT_BANNER_MAP.keys():
        listener_thread = threading.Thread(target=start_listener, args=(HOST, port))
        listener_thread.daemon = True
        listener_threads.append(listener_thread)
        listener_thread.start()
    
    print(f"[*] {len(listener_threads)} threads running.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[*] Closing honeypot.")
        write_log("[*] Honeypot successfully closed.", MAIN_LOG_FILE)
    except Exception as e:
        critical_error = f"Honeypot starting error: {e}"
        print(f"[!!] {critical_error}")
        write_log(f"[!!] {critical_error}", MAIN_LOG_FILE)
