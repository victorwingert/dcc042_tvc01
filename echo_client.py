import socket

HOST = 'localhost'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Conectado ao servidor em {HOST}:{PORT}")

    while True:
        mensagem = input("Digite uma mensagem ('sair' para encerrar): ")

        if mensagem.lower() == 'sair':
            break

        s.sendall(mensagem.encode())
        resposta = s.recv(1024).decode()

        print(f"Servidor respondeu: {resposta}")
