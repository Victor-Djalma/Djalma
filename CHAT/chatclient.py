import socket
import sys
import configparser


config = configparser.ConfigParser() # aqui crio um objeto, que nos permite ler e manipular esse tipo de arquivo de configuração
config.read('config.txt')# aqui eu permito que meu objeto leia o arquivo

HOST = config.get('DEFAULT', 'HOST')# aqui o objeto vai pegar o host que esta dentro do arquivo
PORT = int(config.get('DEFAULT', 'PORT'))# aqui o objeto vai pegar a porta que esta dentro do arquivo

if len(sys.argv) <2:
    print("uso: script.py arguento")
    sys.exit(1)
msg = ''.join(sys.argv[1:])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #criamos um socket TCP/IP
    s.connect((HOST, PORT))# conectando o cliente ao servidor
    s.sendall(msg.encode()) # Envia a mensagem
    data = s.recv(1024)# Recebe a resposta do servidor
    print(f"Resposta do servidor: {data.decode()}")
