import socket
import os
import threading
from datetime import datetime
from clientClass import Client

#gloabl vars
is_server_open = False
lista_client = list()

def aspettaClient(server_socket : socket.socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print("[SERVER] Connessione accettata da:", client_address)
        nome_client = client_socket.recv(1024).decode()
        nuovo_client = Client(client_socket, nome_client, client_address)
        lista_client.append(nuovo_client)
        
        t_client = threading.Thread(target=ascoltaClient, args=(nuovo_client,))
        t_client.start()
        
def ascoltaClient(client : Client):
    #thread_io : threading.Thread, da inserire come argomento
    print("[SERVER] Si è connesso: " + str(client.nome))
    client_socket=client.clientSocket
    nomeOutput = client.nome + "-" + str(datetime.now().strftime("%Y-%m-%d %H.%M.%S"))
    while True:
        data = client_socket.recv(1024)
        decoded_data = str(data.decode('utf-8'))
        newLog = open(nomeOutput, "a")
        newLog.write(decoded_data)
        newLog.close()
        
def main():
    print("[DIO] Per chi usa questo programma non c'è ne inferno ne paradiso")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    
    server_socket.listen(25)

    is_server_open = True
    print("[SERVER] Il server è in ascolto su {}:{}".format(*server_address))

    threading.Thread(target=aspettaClient, args=(server_socket,)).start()



#########################
if __name__== "__main__":
   main()                
#########################