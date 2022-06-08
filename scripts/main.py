import functions

logsPath = "scripts/logs/"

tempLog = functions.recording()

tempLogName = functions.calcualteDataAndHour()

newLog = open(logsPath+tempLogName, "w")
newLog.write(str(tempLog))
newLog.close()