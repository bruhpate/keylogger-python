import functions

def main():
    logsPath = "scripts/logs/"

    tempLog = functions.recording()

    tempLogName = functions.calcualteDataAndHour()

    functions.writeToFile(logsPath,tempLogName,tempLog)




##########################
if __name__== "__main__":
   main()                
##########################   