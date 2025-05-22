import socket
import datetime

HOST = '0.0.0.0'
PORT = 2222
LOG_FILE = "log.txt"

def log_data(data):
    with open(LOG_FILE, "a") as f:
        f.write(data + "\n")

def run_honeypot():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[+] SSH Honeypot listening on port {PORT}...")

    while True:
        client_socket, addr = server_socket.accept()
        ip, port = addr
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_data(f"\n=== Connection from {ip}:{port} at {timestamp} ===")
        print(f"[!] Connection from {ip}:{port} at {timestamp}")

        try:
            banner = "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n"
            client_socket.sendall(banner.encode())

            client_socket.sendall(b"login as: ")
            username = client_socket.recv(1024).decode().strip()
            log_data(f"[{ip}] Username attempt: {username}")

            client_socket.sendall(b"Password: ")
            password = client_socket.recv(1024).decode().strip()
            log_data(f"[{ip}] Password attempt: {password}")

            client_socket.sendall(b"Permission denied, please try again.\r\n$ ")

            while True:
                client_socket.sendall(b"$ ")
                data = client_socket.recv(1024)
                if not data:
                    break
                command = data.decode().strip()
                log_data(f"[{ip}] Command: {command}")

        except Exception as e:
            log_data(f"[{ip}] ERROR: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    run_honeypot()
