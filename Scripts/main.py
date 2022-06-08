import functions
import smtplib
from threading import Timer
from datetime import datetime
from lib import keyboard

logsFolder = "/logs/"

logsCounter = functions.calculateLenghtOfLogs("/logs/")

tempLog = functions.recording()


