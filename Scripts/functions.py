from asyncio import sleep
from lib import keyboard
from datetime import datetime
import os

def recording():
    return keyboard.record(until=('escape + shift'))

def calculateLenghtOfLogs(dir):
    return len(os.listdir(dir))
