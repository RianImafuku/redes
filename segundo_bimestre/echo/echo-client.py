import socket

IP_SERVIDOR = "172.16.100.56"
PORTA_SERVIDOR = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#solicitamos a conexão ao servidor usando o comando connect
s.connect((IP_SERVIDOR, PORTA_SERVIDOR))

#criamos uma variavel com a mensagem que sera enviada ao servidor, deve ser uma string em bytes e nao conter acentos ou cedilha
mensagem = b"ola marileine"
print(f"gritei pro server: {mensagem.decode('utf-8')}")

#mandamos a mensagem ao servidor
s.sendall(mensagem)

#recebemos de volta e imprimimos na tela
dados = s.recv(1024)
print(f"e ele respondeu: {dados.decode('utf-8')}")