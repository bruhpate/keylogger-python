import functions

def main():
    logsPath = "scripts/logs/"  #logs path where output is stored

    functions.checkLogsPath(logsPath)   #check if the output storage is existing

    tempLog = functions.recording()     #recording keys... and save it in a variable

    tempLogName = functions.calcualteDataAndHour()      #from date and hour create the new file name where storage the output

    functions.writeToFile(logsPath,tempLogName,tempLog) #write into a new file the output 




#########################
if __name__== "__main__":
   main()                
#########################