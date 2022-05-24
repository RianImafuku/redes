import socket

IP_SERVIDOR = "172.16.100.50"
PORTA_SERVIDOR = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Solicitamos a conexão ao servidor usando o comando
# connect
s.connect((IP_SERVIDOR, PORTA_SERVIDOR))

# Criamos uma variável com o mensagem que será enviada ao
# servidor. Deve ser um string em bytes e não conter
# acentos ou cedilha
mensagem = b"pamonha"
print(f"Gritei pro servidor: {mensagem.decode('utf-8')}")

# Mandamos a mensagem ao servidor
s.sendall(mensagem)

# Recebemos de volta e imprimimos na tela
dados = s.recv(1024)
print(f"E ele respondeu: {dados.decode('utf-8')}")
