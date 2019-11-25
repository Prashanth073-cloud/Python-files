#Name: Prashanth Chintala
#CNumber: C0759844
#Date: 11/15/2019
#Question: 2

def main():
    print("\n                         STUDENT COUNT BY DEPARTMENT                          ")
    filePointer = open("enrollment.csv","r")
    departmentFileList = []
    programFileList = []
    freshmanCount = 0
    sophomoreCount = 0
    juniorCount = 0
    count = 0
    simpleCount = 0
    countUpdated = False
    savedPgmFileListLength = 0

    
    outputFilePointer = open("output.txt","w")
    for fileLines in filePointer:
        fileLinesArray = fileLines.split(",")
        #print(fileLinesArray)

        #This block will print department name if it is not present in the list
        if(len(departmentFileList) ==0 and fileLinesArray[3] not in departmentFileList):   #checking if the department is present in the list,if it is not then printing department
            departmentFileList.append(fileLinesArray[3]) #adding department to list
            print(fileLinesArray[3]+"\n\n")              #prints department name
            outputFilePointer.write(fileLinesArray[3]+"\n\n")
        #This will print only firsr program name when the simpleCount = 0
        if(simpleCount == 0):
            print(fileLinesArray[4]+"\n")
            outputFilePointer.write(fileLinesArray[4]+"\n")
            savedPgmFileListLength = len(programFileList)
            simpleCount+=1
            programFileList.append(fileLinesArray[4])
            countUpdated = False #we are using count to update the freshman,sophomore and junior count values to the screen

        #This block will print program name if it is not present and also  it updtes the count values to the screen
        if(fileLinesArray[4] not in programFileList):
            savedPgmFileListLength = len(programFileList)
            programFileList.append(fileLinesArray[4])
            countUpdated = False
            simpleCount+=1

            #This will print count values and also the department names accordingly
            if(countUpdated == False and savedPgmFileListLength+1 == len(programFileList)):
                print("                                          Freshman: ",freshmanCount)
                outputFilePointer.write("                                          Freshman: "+str(freshmanCount)+"\n")
                print("                                          Sophomore: ",sophomoreCount)
                outputFilePointer.write("                                          Sophomore: "+str(sophomoreCount)+"\n")
                print("                                          Junior: ",juniorCount)
                outputFilePointer.write("                                          Junior: "+str(juniorCount)+"\n")
                print(programFileList[simpleCount-2]+" TOTAL  ",freshmanCount+sophomoreCount+juniorCount,"\n")
                outputFilePointer.write(programFileList[simpleCount-2]+" TOTAL  "+str(freshmanCount+sophomoreCount+juniorCount)+"\n\n")

                if(len(departmentFileList)>0 and fileLinesArray[3] not in departmentFileList):
                    departmentFileList.append(fileLinesArray[3])
                    print(fileLinesArray[3]+"\n\n")
                    outputFilePointer.write(fileLinesArray[3]+"\n\n")
                    print(fileLinesArray[4]+"\n")
                    outputFilePointer.write(fileLinesArray[4]+"\n")
                else:
                    print(fileLinesArray[4]+"\n")
                    outputFilePointer.write(fileLinesArray[4]+"\n")
                    
                
                freshmanCount = 0
                sophomoreCount = 0
                juniorCount = 0
                count+=1
                countUpdated=True
        

        #This will count the freshman,sophomore and junior values 
        if(int(fileLinesArray[5]) == 1):
            freshmanCount+=1
        if(int(fileLinesArray[5]) == 2):
            sophomoreCount+=1
            #print(freshmanCount)
        if(int(fileLinesArray[5]) ==3):
            juniorCount+=1

    #It will print last program name values after exiting the loop
    print("                                          Freshman: ",freshmanCount)
    outputFilePointer.write("                                          Freshman: "+str(freshmanCount)+"\n")
    print("                                          Sophomore: ",sophomoreCount)
    outputFilePointer.write("                                          Sophomore: "+str(sophomoreCount)+"\n")
    print("                                          Junior: ",juniorCount)
    outputFilePointer.write("                                          Junior: "+str(juniorCount)+"\n")
    print(programFileList[simpleCount-1]+" TOTAL  ",freshmanCount+sophomoreCount+juniorCount,"\n")
    outputFilePointer.write(programFileList[simpleCount-1]+" TOTAL  "+str(freshmanCount+sophomoreCount+juniorCount)+"\n")






main()
