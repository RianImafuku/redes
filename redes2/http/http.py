import socket
import threading

#mudar para adaptar ao desejado, de exemplo to usando "localhost" na porta 5000
ip = '127.0.0.1'
port = 5000
answer = """
HTTP/1.1 200 Ok
Content-Type: text/html
Content-Length: {size}
{body}"""

server_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_test.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server_test.bind((ip, port))
server_test.listen(10)
print('service ip address: {}:{}'.format(ip, port))

def client(client_socket):
    request = client_socket.recv(4096).decode()
    client_socket.send(answer.format(size = len(request), body = request).encode())
    #close
    client_socket.close()

#teste - deu certo
while True:
    client_sock, address = server_test.accept()
    print('received connection from: {}:{}'.format(address[0], address[1]))
    handler = threading.Thread(
        target = client,
        args = (client_sock,))
    handler.start()