from math import sqrt

UserResponse = input("Do you have another student to enter[Y/N]? ")

#initialization
StudentsGradeSum = 0
StudentsCount = 0
MaxStudentGrade=0
MinStudentGrade=0
AverageStudentGrade = 0
SavedAverageGrade =0
SDSum = 0
StandardDeviation = 0


#checking for user response
while(UserResponse == "Y" or UserResponse =="y"):
    StudentsCount+=1
    StudentsGrade = float(input("Enter Student"+str(StudentsCount)+" final percentage grade: "))

    if(StudentsCount ==1):
        MinStudentGrade = StudentsGrade
        MaxStudentGrade = StudentsGrade

    StudentsGradeSum = StudentsGradeSum+StudentsGrade
    UserResponse = input("Do you have another student to enter[Y/N]? ")
    #checking for max and min
    if(StudentsCount!=1 and StudentsGrade>MaxStudentGrade):
        MaxStudentGrade = StudentsGrade
    if(StudentsCount!=1 and StudentsGrade<MinStudentGrade):
        MinStudentGrade = StudentsGrade

    AverageStudentGrade = StudentsGradeSum/StudentsCount
    SavedAverageGrade = AverageStudentGrade
        



StandardDeviationResponse = input("Would you like to include standard deviation in your summary statistics[Y/N]? ")

if(StandardDeviationResponse == "n" or StandardDeviationResponse == "N"):
    print("MAX Student grade is ",MaxStudentGrade,"%")
    print("MIN Student grade is ",MinStudentGrade,"%")
    print("AVERAGE Student grade is ",AverageStudentGrade)
else:
    print("Please re-enter the same percentage grades as you previously did for each student")
    StudentsGradeSum = 0
    for StudentsEnterCount in range(StudentsCount):
        StudentsGrade = float(input("Student "+str(StudentsEnterCount+1)+str(": ")))
        
        SDSum = SDSum +((StudentsGrade - SavedAverageGrade)**2);

        if(StudentsEnterCount ==0):
            MinStudentGrade = StudentsGrade
            MaxStudentGrade = StudentsGrade

        StudentsGradeSum = StudentsGradeSum + StudentsGrade

        if(StudentsEnterCount!=0 and StudentsGrade>MaxStudentGrade):
            MaxStudentGrade = StudentsGrade
        if(StudentsEnterCount!=0 and StudentsGrade<MinStudentGrade):
            MinStudentGrade = StudentsGrade

        AverageStudentGrade = StudentsGradeSum/StudentsCount

    StandardDeviation = sqrt(SDSum/StudentsCount)
   
    print("Standarad deviation is ",format(StandardDeviation,'.2f'))    
    print("MAX Student grade is ",MaxStudentGrade,"%")
    print("MIN Student grade is ",MinStudentGrade,"%")
    print("AVERAGE Student grade is ",AverageStudentGrade)
        
    
