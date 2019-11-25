#Name: Prashanth Chintala
#CNumber: C0759844
#date:11/14/2019
#Quesiton:1

from decimal import Decimal,ROUND_HALF_UP


def main():
    usersChoice = menu()
    usersChoiceMethod(usersChoice)




def menu():
    print("Welcome to Prashanth's application!")
    print("***********************************\n")
    print("MENU:")
    print("(D)elete a record")
    print("(I)nsert a record")
    print("(F)ind matching records")
    print("(S)tatistical Data")
    print("(E)xit program")
    print("***********************************\n")
    usersChoice = input("Please enter your choice: ")
    return usersChoice


def insertInToFile():

    insertList=[]
    firstName = input("Please enter Student First Name: ")
    lastName = input("Please enter Student Last Name: ")
    grade = float(input("Please enter student grade: "))


    filePointer = open("grades.csv","a")
    filePointer.write("\n"+firstName+",")
    filePointer.write(lastName+",")
    filePointer.write(str(Decimal(grade).to_integral_value(rounding=ROUND_HALF_UP))+"\n")
    filePointer.close()

    filePointer = open("grades.csv","r")
    fileList = filePointer.readlines()
    fileList.sort()
    filePointer.close()
    #print(fileList)

    filePointer = open("grades.csv","w")
    for lines in fileList:
        if(lines!="\n"):
            filePointer.write(lines)
    filePointer.close()
    
    

    print("\nRecord successfully inserted:",firstName,",",lastName,",",round(Decimal(grade).to_integral_value(rounding=ROUND_HALF_UP)),"\n")

    main()


def findTheStringFromFile():
   nameFound = False
   foundRecord = ""
   firstName =  input("Please enter Student First Name: ")
   lastName = input("Please enter Student Last Name: ")

   filePointer = open("grades.csv","r")
   
   for fileLines in filePointer:
       fileLines = fileLines.rstrip()
       lineArray = fileLines.split(",")
       if(lineArray[0] == firstName and lineArray[1] == lastName):
           nameFound = True
           foundRecord = foundRecord+ lineArray[0]+","+lineArray[1]+","+lineArray[2]+"\n"

   filePointer.close()
   print("\nMatching Redord(s):\n")
   print(foundRecord)

   main()


def deletingARecord():

    recordFound = False

    firstNameToDelete = input("Please enter the first name: ")
    lastNameToDelete = input("Please enter the last name: ")
    
    filePointer = open("grades.csv","r")
    fileArray = filePointer.readlines()
    filePointer.close()
 
    #print(fileArray)

    filePointer = open("grades.csv","w")
    fileLinesCount = 0
    for fileLines in fileArray:
        rangeOfArray = len(fileArray)

        if(fileLinesCount <=rangeOfArray):
            singleRecord=fileArray[fileLinesCount] #single record from list of records

        fileLinesCount+=1
        singleRecord = singleRecord.rstrip() #removes new line at the end of the record
        singleRecordArray = singleRecord.split(",")
        #print(singleRecordArray)
        firstNameInRecord=singleRecordArray[0]
        lastNameInRecord = singleRecordArray[1]
        #print(firstNameInRecord,lastNameInRecord)
        if(recordFound ==True or (firstNameToDelete != firstNameInRecord and lastNameToDelete != lastNameInRecord)):
            filePointer.write(singleRecord+"\n")
        else:
            recordFound = True

    if(recordFound == True):
        print("\nSuccessfully deleted the record!!!!\n")
    else:
        print("\nNo data found with that name\n")
    filePointer.close()

    main()


def statistics():
    fileLinesCount = 0
    gradeSum = 0
    averageGrade = 0
    maxGrade = 0
    minGrade = 0
    gradeACount = 0
    gradeBCount = 0
    gradeCCount = 0
    gradeDCount = 0
    gradeFCount = 0
     
    
    filePointer = open("grades.csv","r")
    #print(filePointer.)
    for fileLines in filePointer:
        fileLines = fileLines.rstrip()
        record = fileLines.split(",")  #splitting record
        #print(record)

        #max and min code
        if(fileLinesCount == 0):       #initializing max and min grade with initial file grade values
            maxGrade = int(record[2])  
            minGrade = int(record[2]) 
        else:
            if(int(record[2]) > int(maxGrade)):  #checking if current grade value of file is greater than the max grade,if it is greater, then saving the greater value in max grade
                maxGrade = int(record[2])
                
            if(int(record[2]) < minGrade):      #checking if current grade value of file is less than the min grade,if it is less,then saving the lesser value in min grade
                minGrade = int(record[2])
                
        fileLinesCount+=1                    #incrementing filesLineCount to calculate number of records in the file
        gradeSum = gradeSum + int(record[2])  #taking sum of all the grades

        #grades category count code
        gradeValue = int(record[2])
        if(gradeValue>=80 and gradeValue<=100):
            gradeACount+=1
        elif(gradeValue>=70 and gradeValue<=79):
            gradeBCount+=1
        elif(gradeValue>=60 and gradeValue<=69):
            gradeCCount+=1
        if(gradeValue>=50 and gradeValue<=59):
            gradeDCount+=1
        if(gradeValue>=0 and gradeValue<=49):
            gradeFCount+=1
            

    averageGrade = round(gradeSum/fileLinesCount,1)    #calculating average grade
    print("AVG",str(averageGrade)+str("%"))   
    print("MAX:",str(maxGrade)+str("%"))
    print("MIN:",str(minGrade)+str("%"))
    print("A grades:",gradeACount)
    print("B grades:",gradeBCount)
    print("C grades:",gradeCCount)
    print("D grades:",gradeDCount)
    print("F grades:",gradeFCount)

    filePointer.close()
    main()
        
        
        

def usersChoiceMethod(usersChoice):
    usersChoice = usersChoice.upper()
    if(usersChoice == "I"):
        insertInToFile()
    elif(usersChoice == "F"):
        findTheStringFromFile()
    elif(usersChoice == "E"):
        print("Thank you for using Prashanth's grade application!")
    elif(usersChoice == "D"):
        deletingARecord()
    elif(usersChoice =="S"):
        statistics()
    else:
        print("\nInvalid menu selection.Please try again: \n")
        menu()
   

main()
