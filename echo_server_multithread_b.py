import socket
import threading
import queue

HOST = 'localhost'
PORT = 5000
MAX_THREADS = 10

fila_clientes = queue.Queue()
threads_ocupadas = 0
lock = threading.Lock()

def tratar_cliente(conn, addr):
    global threads_ocupadas
    with conn:
        print(f"[Atendendo] {addr}")
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
        except:
            pass
        print(f"[Desconectado] {addr}")
    
    with lock:
        threads_ocupadas -= 1

def worker():
    while True:
        conn, addr = fila_clientes.get()
        tratar_cliente(conn, addr)
        fila_clientes.task_done()

def servidor():
    global threads_ocupadas

    for _ in range(MAX_THREADS):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[Servidor] Escutando em {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()

            with lock:
                if threads_ocupadas >= MAX_THREADS:
                    print(f"[Lotado] {addr} recusado")
                    try:
                        conn.sendall("Servidor ocupado. Tente mais tarde.".encode())
                    except:
                        pass
                    conn.close()
                else:
                    threads_ocupadas += 1
                    fila_clientes.put((conn, addr))

if __name__ == '__main__':
    servidor()