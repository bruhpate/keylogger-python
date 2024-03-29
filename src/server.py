import socket
import os
import time
import threading
from datetime import datetime
from clientClass import Client

#gloabl vars
lista_client = list()
evento = threading.Event()

def aspettaClient(server_socket : socket.socket):
    lista_thread_client = list()
    while evento.is_set() == False:
        client_socket, client_address = server_socket.accept()

        print("[SERVER] Connessione accettata da:", client_address)

        nome_client = client_socket.recv(1024).decode()
        nuovo_client = Client(client_socket, nome_client, client_address)
        lista_client.append(nuovo_client)
        
        t_client = threading.Thread(target=ascoltaClient, args=(nuovo_client,))
        t_client.start()

        t_verifica_collegamento = threading.Thread(target=verificaCollegamento, args=(nuovo_client,))
        t_verifica_collegamento.start()

        lista_thread_client.append(t_client)
    for i in lista_thread_client:
        print("[SERVER]","chiusura di tutti i thread")
        i.join()
        lista_thread_client.remove(i)
        
def ascoltaClient(client : Client):
    #thread_io : threading.Thread, da inserire come argomento

    print("[SERVER] Si è connesso: " + str(client.nome))
    client_socket=client.clientSocket
    nomeOutput = client.nome + "-" + str(datetime.now().strftime("%Y-%m-%d %H.%M.%S"))
    while isVivo(client):
        try:
            data = client_socket.recv(1024)
            decoded_data = str(data.decode('utf-8'))
            newLog = open(nomeOutput, "a")
            newLog.write(decoded_data)
            newLog.close()
        except:
            print(client.nome,"si è disconesso")
        
def listaClientToString():
    count = 1
    for i in lista_client:
        print(count,i.nome,i.indirizzo)
        count+=1

def isVivo(obj : Client):
    for i in lista_client:
        if i == obj:
            return True
    return False

def rimuoviTuttiIClient():
    for i in lista_client:
        lista_client.remove(i)

def verificaCollegamento(client : Client):
    while isVivo(client):
        try:
            client.clientSocket.sendall('a'.encode())
        except:
            client.clientSocket.close()
            lista_client.remove(client)
            break
        time.sleep(15)        

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    
    server_socket.listen(25)

    print("[SERVER] Il server è in ascolto su {}:{}".format(*server_address))
    print("[SERVER] Comandi: 'list' o 'l' ottieni la lista dei client connessi")
    print("                  'close-server' o 'cs' ottieni la lista dei client connessi")



    t_aspetta_client = threading.Thread(target=aspettaClient, args=(server_socket,))
    t_aspetta_client.daemon = True
    t_aspetta_client.start()

    while evento.is_set() == False:
        command = input()
        if command == "list" or command == "l":
            listaClientToString()
        if command == "close-server" or command == "cs":
            evento.set()
            rimuoviTuttiIClient()
            server_socket.close()
            print("Server chiuso")
#########################
if __name__== "__main__":
   main()                
#########################
