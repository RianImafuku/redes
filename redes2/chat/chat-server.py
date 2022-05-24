import socket
from _thread import *

IP = "127.0.0.1"
PORTA = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((IP, PORTA))
server.listen(100)

lista_de_clientes = []

#função que transmite uma mensagem a todos os clientes conectados
def broadcast(mensagem, conexao):
    for cliente in lista_de_clientes:
        if cliente != conexao:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                if cliente in lista_de_clientes:
                    lista_de_clientes.remove(cliente)

def atender_cliente(conexao, endereco):
    conexao.send(b"Bem-vindo(a) ao chat de ADS Unimar!!")
    while True:
        try:
            mensagem = conexao.recv(2048)
            if mensagem:
                #se a mensagem recebida tem conteúdo
                msg_envio = ">"+endereco[0]+">: " + mensagem.decode("utf-8")
                print(msg_envio)
                broadcast(msg_envio, conexao)
            else:
                print("mensagem vazia")
                if conexao in lista_de_clientes:
                    lista_de_clientes.remove(conexao)                
        except Exception as e:
            print(str(e))
            continue

while True:
    conexao, endereco = server.accept()
    # adicionar a nova conexão á lista de clientes
    lista_de_clientes.append(conexao)
    # Imprime na tela do servidor o ip da nova conexão
    print(endereco[0] + " conectado!")
    # Inicia uma nova thread para atender a conexão
    start_new_thread(atender_cliente, (conexao, endereco))

conexao.close
server.close()
