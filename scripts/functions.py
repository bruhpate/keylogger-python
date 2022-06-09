from lib import keyboard
from datetime import datetime
import os

def checkLogsPath(path):
    if os.path.exists(path) == False:
        os.mkdir(path)

def recording():
    return keyboard.record(until=('ctrl + esc + pause + right'))

def calcualteDataAndHour():
    tempTime = datetime.now()
    return str(tempTime.strftime("%Y-%m-%d %H:%M:%S"))

def writeToFile(lPath, lName, l):
    newLog = open(lPath+lName, "w")
    newLog.write(str(l))
    newLog.close()