import socket
import datetime

HOST = '0.0.0.0'
PORT = 23 #Telnet
LOG_FILE = "honeypot_log.txt"

def write_log(message):    
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def start_honeypot(host, port):
    print(f"[*] Honeypot iniciando na porta {port}...")
    write_log(f"Honeypot iniciado em {host}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        while True:
            try:
                conn, addr = s.accept()
                with conn:
                    log_message = f"Conexão recebida de: {addr[0]}:{addr[1]}"
                    print(log_message)
                    write_log(log_message)
                    conn.sendall(b"Welcome to the Telnet server!\r\nUsername: ")
            except Exception as e:
                error_message = f"Erro: {e}"
                print(f"[!] {error_message}")
                write_log(error_message)

if __name__ == "__main__":
    try:
        start_honeypot(HOST, PORT)
    except KeyboardInterrupt:
        print("\n[*] Desligando o honeypot.")
        write_log("Honeypot desligado pelo usuário.")
    except Exception as e:
        critical_error = f"Erro crítico ao iniciar o honeypot: {e}"
        print(f"[!!] {critical_error}")
        write_log(critical_error)
