from asyncio import sleep
from lib import keyboard
from datetime import datetime
import os

def recording():
    return keyboard.record(until=('escape + shift'))

# def calculateLenghtOfLogs(dir):
#     return len(os.listdir(dir))

def calcualteDataAndHour():
    return (datetime.year + '/' + datetime.month + '/' + datetime.day + ' / ' + datetime.hour + '/' + datetime.minute + '/' + datetime.second + ".txt")    
