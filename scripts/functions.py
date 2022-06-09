from lib import keyboard
from datetime import datetime
import os

def checkLogsPath(path):
    os.path.exists(path)
        



def recording():
    return keyboard.record(until=('escape + shift'))

def calcualteDataAndHour():
    tempTime = datetime.now()
    return str(tempTime.strftime("%Y-%m-%d %H:%M:%S"))

def writeToFile(lPath, lName, log):
    newLog = open(lPath+lName, "w")
    newLog.write(str(log))
    newLog.close()