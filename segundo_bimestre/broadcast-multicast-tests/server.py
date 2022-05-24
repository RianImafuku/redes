# Importamos a biblioteca de sockets do Python
from ast import arg
import socket
# Para poder suportar multiplas conexões, usamos threads
import threading

# função executada para cada nova conexao criando uma thread
def atenderCliente(cliente, endereco):
    print(f"conexao ao cliente {endereco}")
    while True:
        dadosRecebidos = cliente.recv(1024)
        if not dadosRecebidos:
            break
    mensagem = dadosRecebidos.decode('utf-8')
    print(f"O cliente {endereco} enviou: {mensagem}")

# Declaramos uma variável string com o nosso endereço IP
MEU_IP = "127.0.0.1"
# Declaramos uma variável numérica com o número da porta que
# nosso server vai usar. Deve ser maior que 1023 e menor
# que 65535
PORTA = 12345

# Criamos o socket para o nosso servidor de eco
# O parâmetro AF_INET indica que estamos criando um
#   socket para redes IP tradicionais (IPv4)
# O parâmetro SOCK_STREAM indica que queremos um socket
#   de fluxo, usando o TCP como protocolo de transporte.
#   A outra opção seria SOCK_DGRAM para uso com UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# Executa o comando bind do objeto socket (chamado "s")
# passando como parâmetro o IP e o número da porta
s.bind((MEU_IP, PORTA))

# Começa a "escutar" por possíveis conexões
s.listen(20)
print("Aguardando por conexões...")
print(f"meu ip: {MEU_IP} e porta: {PORTA}")

while True:
    # O comando accept() aceita uma solicitação de conexão
    # vinda de um cliente. Ele retorna um objeto representando
    # a conexão (variável "cliente") e o endereço do cliente
    # (variável "endereco")
    cliente, endereco = s.accept()
    print(f"Conexão realizada com o cliente {endereco}")
    threading.Thread(target=atenderCliente, arg=(cliente, endereco))