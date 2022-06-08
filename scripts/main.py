from venv import create
import functions
import smtplib
from threading import Timer
from datetime import datetime

logsFolder = "/logs/"

tempLog = functions.recording()

tempLogName = functions.calcualteDataAndHour()

newLog = open("scripts/logs/"+str(tempLogName), "w")
newLog.write(str(tempLog))
newLog.close()


