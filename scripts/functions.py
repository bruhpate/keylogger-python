from lib import keyboard    #for manipulate the keyboard
from datetime import datetime   #for using date and hour
import os   #file manager
import re

def checkLogsPath(path):
    if os.path.exists(path) == False:
        os.mkdir(path)

def recording():
    return keyboard.record(until=('space'))

def calcualteDataAndHour():
    tempTime = datetime.now()
    return str(tempTime.strftime("%Y-%m-%d %H.%M.%S"))

def writeToFile(lPath, lName, l):
    newLog = open(lPath+lName, "a")
    newLog.write(str(l))
    newLog.close()