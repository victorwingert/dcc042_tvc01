import socket
import threading

HOST = 'localhost'
PORT = 5000

def tratar_cliente(conn, addr):
    print(f"[+] Novo cliente conectado: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    print(f"[-] Cliente desconectado: {addr}")

# criação do socket principal

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor ouvindo em {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=tratar_cliente, args=(conn, addr))
        thread.start()