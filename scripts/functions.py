from lib import keyboard
from datetime import datetime

def recording():
    return keyboard.record(until=('escape + shift'))

def calcualteDataAndHour():
    tempTime = datetime.now()
    return str(tempTime.strftime("%Y-%m-%d %H:%M:%S"))