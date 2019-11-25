#Name:Prashanth Chintala,CNumber:C0759844,Question:015,Date:11/5/2019


#Initializing variables
scoreAverage = 0
letterGrade = 'A'
testScoreCount = 0
testScore = 0

#main function
def main():
    testScore_input() #calling testscore input function
    calc_average(100,89,79,69,59) #calling calulate average funtion



#This function will take test score as an parameter and returns letter grade 
def determine_grade(testScore):
    if(testScore>=90 and testScore<=100):
        letterGrade ='A'
    elif(testScore>=80 and testScore<=89):
        letterGrade ='B'
    elif(testScore>=70 and testScore<=79):
        letterGrade ='C'
    elif(testScore>=60 and testScore<=69):
        letterGrade ='D'
    elif(testScore<60):
        letterGrade ='F'

    return letterGrade





#This function will ask user to enter test score five times and send this test score to dertermine_grade() to get grades of it and displays it
def testScore_input():
    
    for x in range(1,6):
        testScore = int(input("Please enter your score "+str(x)+str(' ')))
        letterGrade = determine_grade(testScore)
        print("Letter grade for test score",testScore,"is ",letterGrade)

#This function will take five test scores as parameters and calculates average of those test scores
def calc_average(testScore1,testScore2,testScore3,testScore4,testScore5):
    scoreAverage = (testScore1+testScore2+testScore3+testScore4+testScore5) / 5
    print("The average of test score is ",scoreAverage)
    

main()
