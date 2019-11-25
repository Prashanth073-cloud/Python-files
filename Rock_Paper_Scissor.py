#Name:Prashanth Chintala,CNumber:C0759844,Question:021,Date:11/5/2019

#importing random function
import random

#Initializing variables
randomNumber = 0
computerChoice = 'UnKnown'
userChoice = 0

#main function
def main():
    randomNumber = random.randint(1,3)   #It will generate random number between 1 and 3
    if(randomNumber == 1):
        computerChoice = "Rock"
    elif(randomNumber == 2):
        computerChoice = "Paper"
    elif(randomNumber == 3):
        computerChoice = "Scissors"
    
    userChoice = int(input("Please enter your choice. Enter 1 for Rock . Enter 2 For Paper. Enter 3 for Scissors: "))  #This will ask for users choice
    print("Computers choice is ",computerChoice) #printing computers choice
    if(randomNumber == 1 and userChoice == 3):
        print("Computer won the game")
    elif(randomNumber == 3 and userChoice == 1):
        print("You won the game")
    elif(randomNumber ==3 and userChoice == 2):
        print("Computer won the game")
    elif(randomNumber == 2 and userChoice == 3):
        print("You won the game")
    elif(randomNumber ==1 and userChoice == 2):
        print("Computer won the game")
    elif(randomNumber == 2 and userChoice == 1):
        print("You won the game")
    elif(randomNumber == userChoice):
        drawnChoice = int(input("Game is drawn. Do you want to play game again? Enter 1 to Play Again. Enter 2 to Quit: "))
        if(drawnChoice == 1):
            main()                 #calling main function again if user wanna play again when score is drawn
        else:
            print("Your game is drawn")
  


