#Name:Prashanth Chintala
#CNumber: C0759844
#Date:12/4/2019
#Question:Q7

def main():
    examAnswersList = ['a','c','a','a','d','b','c','a','c','b','a','d','c','a','d','c','b','b','d','a'] #ExamAnsewers list
    studentsAnswersList = []
    gradesFile = open('grades.csv','r') #opening grades file
    correctMarksCount = 0
    inCorrectMarksCount = 0
    inCorrectQuestionsList = []

    #storing students grades from file to list
    for fileLines in gradesFile:
        fileLines = fileLines.rstrip()
        studentsAnswersList.append(fileLines)
    #print(studentsAnswersList)
    gradesFile.close()
    
    #correcting users answers with examsanswerslist
    for answerIndex in range(len(examAnswersList)):
        if(studentsAnswersList[answerIndex] == examAnswersList[answerIndex]):
            correctMarksCount+=1
        else:
            inCorrectQuestionsList.append(answerIndex)
            inCorrectMarksCount+=1

    
    if(correctMarksCount>=15): #if the marks are greater than or equals to 15 then displaying that student is passed message
        print("Student has passed the exam as he answered ",correctMarksCount,"questions correctly")
    else:
        print("Student has failed the exam as he answered only",correctMarksCount,"questions correctly")
    print("Student has answered ",correctMarksCount,"questions correct")
    print("Student has answered ",inCorrectMarksCount,"questions incorrect")
    print("The incorrect questions of students are ",inCorrectQuestionsList)
        
main()
