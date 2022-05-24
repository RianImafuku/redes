#importamos a biblioteca de sockets do python
from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
import socket

#declaramos uma variavel string com nosso endereco de ip
MEU_IP = "172.16.100.56"
# declaramos uma variavel numerica com o numero da porta que nosso servidor vai usar. deve ser maior que 1023 e menor que 65535
PORTA = 12345

#criamos o socket para o nosso servidor de eco
#o parametro AF_INET indica que estamos criando um socket para redes ip tradicionais (ipv4)
#o parâmetro SOCK_STREAM indica que queremos um socket de fluxo, usando o tcp como protocolo de transporte, a outra opção seria SOCK_DGRAM para uso com o UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#executa o comando bind do objeto socket (chamado 's') passando como parametro o ip e a porta
s.bind((MEU_IP, PORTA))
#começa a escutar por possiveis conexoes
s.listen()
print('Aguardando por conexões. . .')

#o comando accept() aceita uma solicitação de conexao vinda de um cliente, ele retorna um objeto representando a conexao (variavel "cliente") e o endereço do cliente (variavel endereco)
cliente, endereco = s.accept()
print(f"conexao realizada com o cliente {endereco}")

while True:
    #recebemos os dados do cliente (1024 bytes no maximo)
    dados = s.recv(1024)
    #se os dados estiverem vazios, quebramos o laço
    if not dados:
        break
    #caso tenhamos dados, enviamos de volta ao cliente fazendo un "eco"
    s.sendall(dados)