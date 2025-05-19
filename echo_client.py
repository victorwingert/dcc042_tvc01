import socket

HOST = 'localhost'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Conectado ao servidor em {HOST}:{PORT}")

    while True:
        msg = input("Mensagem ('sair' para encerrar): ")
        if msg.lower() == 'sair':
            break

        s.sendall(msg.encode())
        data = s.recv(1024).decode()

        print(f"[Servidor]: {data}")

        if data == "Servidor ocupado. Tente mais tarde.":
            break
