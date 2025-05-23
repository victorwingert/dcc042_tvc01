🔁 Echo Server Multithreaded - TVC 1

Este projeto implementa uma aplicação Echo utilizando sockets TCP em Python, com duas versões multithread do servidor, conforme solicitado na disciplina DCC042 - TVC 1.

🧠 Sobre o Projeto

O objetivo é criar um servidor que recebe mensagens de clientes e responde com o mesmo conteúdo (efeito de eco), utilizando duas abordagens diferentes de multithreading.

🗂️ Arquivos

- echo_client.py: Cliente que se conecta ao servidor e envia mensagens.
- echo_server.py: Versão simples do servidor sem multithreading (base).
- echo_server_multithread_a.py: Versão A - Cria uma thread por cliente.
- echo_server_multithread_b.py: Versão B - Usa um pool fixo de 10 threads.

🧵 Versões do Servidor

✅ Versão A – Uma Thread por Cliente

- Cada vez que um cliente se conecta, uma nova thread é criada.
- Quando o cliente se desconecta, a thread termina.
- Boa para testes ou poucos clientes simultâneos.

✅ Versão B – Pool Fixo de 10 Threads

- O servidor cria 10 threads ao iniciar.
- Cada cliente é atendido por uma thread livre.
- Se todas as threads estiverem ocupadas, o servidor recusa a conexão e informa que está ocupado.

▶️ Como Executar

1. Inicie o servidor

    python echo_server_multithread_a.py
    ou
    python echo_server_multithread_b.py

2. Em outro terminal, inicie o cliente

    python echo_client.py

👥 Autores

Este repositório faz parte da entrega do grupo:

- Victor Wingert de Almeida
- Pedro C Sevenini

📄 Observações

- O projeto foi feito utilizando Python.
- Os testes foram realizados localmente com múltiplos terminais para simular conexões simultâneas.
