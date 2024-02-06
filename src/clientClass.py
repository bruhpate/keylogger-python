from datetime import datetime 
from socket import socket 
class Client:
    def __init__(self, socket : socket, nome : str, indirizzo : str):
        self.clientSocket = socket
        self.nome = nome
        self.indirizzo = indirizzo

    def socket(self) -> socket:
        return self.clientSocket

    def nome(self) -> str:
        return self.nome
    
    def indirizzo(self) -> str:
        return self.indirizzo