from asyncio import sleep
from lib import keyboard
from datetime import datetime

def recording():
    return keyboard.record(until=('escape + shift'))

# def calculateLenghtOfLogs(dir):
#     return len(os.listdir(dir))

def calcualteDataAndHour():
    tempTime = datetime.now()
    return str(tempTime.strftime("%Y-%m-%d %H:%M:%S"))