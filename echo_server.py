import socket

HOST = 'localhost'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor ouvindo em {HOST}:{PORT}...")

    conn, addr = s.accept()

    while conn:
        print(f"Conectado por {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
