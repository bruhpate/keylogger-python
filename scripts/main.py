from venv import create
import functions
import smtplib
from threading import Timer
from datetime import datetime

logsPath = "scripts/logs/"

tempLog = functions.recording()

tempLogName = functions.calcualteDataAndHour()

newLog = open(logsPath+tempLogName, "w")
newLog.write(str(tempLog))
newLog.close()