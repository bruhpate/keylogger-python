from venv import create
import functions
import smtplib
from threading import Timer
from datetime import datetime

logsFolder = "/logs/"

tempLog = functions.recording()

#tempLogName = functions.calcualteDataAndHour()

newLog = open("/logs/"+str(2), "w")
newLog.write(tempLog)
newLog.close()


