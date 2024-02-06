from datetime import datetime 
from socket import socket 
class Client:
    def __init__(self, socket, nome, indirizzo):
        self.clientSocket = socket
        self.nome = nome
        self.indirizzo = indirizzo

    def socket(self) -> socket:
        return self.clientSocket

    def nome(self) -> str:
        return self.nome
    
    def indirizzo(self) -> str:
        return self.indirizzo
    
    def nomeOutput(self) -> str:
        return self.indirizzo(self) + str(datetime.now().strftime("%Y-%m-%d %H.%M.%S"))