import socket
import sys
import select

IP = "172.16.100.50"
PORTA = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP, PORTA))

while True:
    entradas = [sys.stdin, server]
    s_entrada, s_saida, s_erro = select.select(entradas, [], [])
    for s in s_entrada:
        if s == server:
            mensagem = server.recv(2048)
            print(mensagem.decode("utf-8"))
        else:
            mensagem = sys.stdin.readline()
            server.send(mensagem.encode())
            sys.stdout.write("<Você")
            sys.stdout.write(mensagem)
            sys.stdout.flush()
server.close()