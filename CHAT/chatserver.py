import socket
import sys
import configparser


config = configparser.ConfigParser() # aqui crio um objeto, que nos permite ler e manipular esse tipo de arquivo de configuração
config.read('config.txt')# aqui eu permito que meu objeto leia o arquivo

HOST = config.get('DEFAULT', 'HOST')# aqui o objeto vai pegar o host que esta dentro do arquivo
PORT = int(config.get('DEFAULT', 'PORT'))# aqui o objeto vai pegar a porta que esta dentro do arquivo

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #criamos um socket TCP/IP
    s.bind((HOST, PORT))# associando o servidor ao host e a porta
    s.listen(1) # sinalizando que o SO esta pronto para receber conexões 
    print(f"Servidor ouvindo em {HOST}:{PORT}...") # imprime uma frase orientando o host e porta que esta sendi utilizado

    conn, addr = s.accept() # definindo um objeto de comunicação e o endereço do cliente 
    with conn:
        print(f"Conexão estabelecida com {addr}")# exibe a conexão estabelecida com tal endereço
        while True:
            data = conn.recv(1024) # a variavel data recebe a resposta do cliente em até 1024 bytes
            if not data: # se não houver dados o programa encerra
                break
            print(f"Cliente: {data.decode()}") # imprime a mensagem do cliente (a função decode converte os bytes recebidos de volta para texto legível)
            msg = input("Servidor: ") # a resposta do servidor é armazenada na variavel msg
            conn.sendall(msg.encode()) # O servidor envia a mensagem digitada de volta para o cliente. A função encode() converte a mensagem em uma sequência de bytes, que é o formato adequado para ser enviado através do socket.
