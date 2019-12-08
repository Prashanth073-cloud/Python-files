#Name: Prashanth Chintala
#CNumber: C0759844
#Date: 11/28/2019
#Question: Q1


global theatreListArray 
theatreListArray = []
global registrationCount #creating global registrationCount
registrationCount = 1

def main():
   populateTheatreMap() #This will initialize the thearelistarray with zeroes
   menu() #This will show the menu to the user
   
#This method will show menu to the user
def menu():
    space = " "
    star = "*"
    print("\nMENU")
    print(space*2,"1. Reserve Seats")
    print(space*2,"2. Reserve Seats with specific row and column")
    print(space*2,"3. Cancel reservation")
    print(space*2,"4. Remove empty seats from specific row")
    print(space*2,"5. Search for reservation")
    print(space*2,"6. Total seats booked")
    print(space*2,"7. Display theatre map")
    print(space*2,"8. Exit application")
    print(star*25)
    userSelection = input("User selection: ")

   
    if(userSelection.isdigit()):  #checking if the user entered a digit%
        methodSelection(int(userSelection))   #This method will call proper method according to the user input 
    else:
        print("Please select options from the menu")
        menu() #if user does not enter digit then we will show the menu to the user again
      

#This method will call appropriate method based on the users selection
def methodSelection(userSelection):
    global theatreListArray
    if(userSelection == 1):  #It will call reserve seats method
        noOfSeats = int(input("Enter number of adjacent seats do you require: "))
        if(noOfSeats>10 or noOfSeats<1):      #checking if the user entered seats between 1 and 10
           print("Please enter the seats between 1 and 10")
           menu()
        else:
           preference = int(input("Prefernce of seating (1 for back, 2 for front): "))
           reserveSeats(theatreListArray,noOfSeats,preference)
    elif(userSelection == 2):  #It will call reserve seats at position method
        noOfSeats = int(input("Enter number of adjacent seats do you require: "))
        row = int(input("Please enter the row number you wish to book: "))
        if(row>8 or row<1):      #checking if the user entered seats between 1 and 10
           print("Please enter the row between 1 and 8")
           menu()
        else:
           seatNumber = int(input("Please enter the column/Seat number you want your seats to begin at: "))
           reserveSeatsAtPos(theatreListArray,noOfSeats,row,seatNumber)
    elif(userSelection == 3):  #It will call cancel seats method
        reservationNumber = int(input("Please enter the reservation number you would like to cancel: "))
        cancelSeats(theatreListArray,reservationNumber)
    elif(userSelection == 4):   #It will call remove empty seats method
         rowToRemoveEmptySeats = int(input("Which row you would like to remove empty seats from: "))
         if(rowToRemoveEmptySeats<1 or rowToRemoveEmptySeats>8):
            print("Please enter the row number between 1 and 8")
            menu()
         else:
            removeEmptySeatsRow(theatreListArray,rowToRemoveEmptySeats)
    elif(userSelection == 5):   #It will call search seats method
        reservationNumber = int(input("Please enter the reservation number you are searching for: "))
        search(theatreListArray,reservationNumber)
    elif(userSelection == 7):  #It will call the method which will print the theatremap
        printTheatreMap()
    elif(userSelection == 6):   #It will call total  seats booked method
        totalBooked(theatreListArray)
    elif(userSelection == 8):   #It will exit from the program
       print("Thanks for using the application!")
        
#This method will reserve seats to the user based on the user preference
def reserveSeats(theatreListArray,noOfSeats,preference):
    seatsRowsCount = 0
    global registrationCount
    seatsBooked = False

    #Arranging two dimensional array based on the preference
    if(preference == 1):   #If preference is 1,taking row as 0,so that sets will be booked from back
         rows = 8           
         columns = 10
         for row in range(rows-1):    #This loop will print rows  
           
            for column in range(columns-1,-1,-1):  #This loop will iterate based on column values in the program
                seatsRowsCount=0
                for zeroCheck in range(noOfSeats):  #This loop is checking whether the noOfSeats wanted by the user is present continously
                    if((column+zeroCheck)<=rows+1 and theatreListArray[row][column+zeroCheck] == 0 and seatsRowsCount!=noOfSeats): 
                        seatsRowsCount+=1  #This statement is written to track whether the rows user want is present consecutively.If the seatsRowsCount and noOfSets are equal then the seats are available continously
                    else:
                        seatsRowsCount=0
                
                if(seatsRowsCount==noOfSeats):   #This condition will come out of the inner loop if required seats are found
                  break
                
            if(seatsRowsCount==noOfSeats):    #This condition will come out of the main loop if required sets are found
                    for zeroCheck in range(noOfSeats):    #This loop will update the two dimensional array with seats by placing registrationCount
                        theatreListArray[row][column+zeroCheck] = registrationCount
                    seatsBooked = True
                        
            
            if(seatsRowsCount==noOfSeats):
                registrationCount+=1
                break
         if(seatsBooked):
               print("\nYou seats have been successfully booked")
         else:
               print("\nSorry,your seats have not been booked.Please enter again")

            
        
    else:                  #If preference is 2,then taking last row which is 8,so that seat will be booked from front
        rows = 8           #taking last row as user wanted to book seats from front row
        columns = 10
        
        for row in range(rows-1,-1,-1):    #This loop will print rows from back which is from 8 by decrementing -1 for every iteration 
           
            for column in range(columns-1,-1,-1):  #This loop will iterate based on column values in the program
                seatsRowsCount=0
                for zeroCheck in range(noOfSeats):  #This loop is checking whether the noOfSeats wanted by the user is present continously
                    if((column+zeroCheck)<=columns-1 and theatreListArray[row][column+zeroCheck] == 0 and seatsRowsCount!=noOfSeats): 
                        seatsRowsCount+=1  #This statement is written to track whether the rows user want is present consecutively.If the seatsRowsCount and noOfSets are equal then the seats are available continously
                    else:
                        seatsRowsCount=0
                
                if(seatsRowsCount==noOfSeats):   #This condition will come out of the inner loop if required seats are found
                  break
                
            if(seatsRowsCount==noOfSeats):    #This condition will come out of the main loop if required sets are found
                    for zeroCheck in range(noOfSeats):    #This loop will update the two dimensional array with seats by placing registrationCount
                        theatreListArray[row][column+zeroCheck] = registrationCount
                        seatsBooked = True     
            
            if(seatsRowsCount==noOfSeats):
                registrationCount+=1
                break
               
        if(seatsBooked):
            print("\nYou seats have been successfully booked")
        else:
            print("\nSorry,your seats have not been booked.Please enter again")  
        

    menu() #This is to show input to the user after booking sets


#This method will book seats at the specified user position
def reserveSeatsAtPos(theatreListArray,noOfSeats,row,seatNumber):
                rows = 8           #taking last row as user wanted to book seats from front row
                columns = 10
                seatsRowsCount = 0
                tempSeatVar = seatNumber
                global registrationCount
 
           

                for zeroCheck in range(noOfSeats):  #This loop repeats for the noOfSeats times user mentioned
                    if((seatNumber-1)<=columns-1 and theatreListArray[row-1][seatNumber-1] == 0 and seatsRowsCount!=noOfSeats): 
                        seatNumber+=1
                        seatsRowsCount+=1  
                    else:
                        seatNumber+=1
                        seatsRowsCount=0
                
                if(seatsRowsCount==noOfSeats):   #if both variables are same then that means user mentioned seats are found 
                  for zeroCheck in range(noOfSeats):    #This loop will update the two dimensional array with seats by placing registrationCount
                        theatreListArray[row-1][(tempSeatVar+zeroCheck)-1] = registrationCount
                  registrationCount+=1
                  print("\n Your seats have booked successfully")
                else:
                   print("\nSorry!!!Your tickets have not been booked.Please try again")
                        
                menu()

#This method will cancel the reservation of the user
def cancelSeats(theatreArray,bookingNumber):
   rows = 8
   columns = 10
   global registrationCount
   registrationFound = False
   
   for row in range(rows):
      for column in range(columns):
         if(theatreListArray[row][column] == bookingNumber):  #It checks  the user entered registration number in the list
            theatreListArray[row][column] = 0
            registrationFound = True

   if(registrationFound == True):
      print("\n Your registration is successfully cancelled")
   else:
      print("\n Sorry! we could not find your registration number.Please try again")
      
   menu()

#This method will search for the registration number in the theatre
def search(theatreListArray,bookingNumber):
   rows = 8
   columns = 10
   global registrationCount
   registrationFound = False
   
   for row in range(rows):
      for column in range(columns):
         if(theatreListArray[row][column] == bookingNumber):   #It checks  the user entered registration number in the list
               if(registrationFound == False):
                  print("SEATS INCLUDED:")
               print("Row: ",row+1,", Seat",column+1)  #It will print the seat numbers which user is searching for
               registrationFound = True
   if(registrationFound == False):
      print("\nSorry! We could not find your registration number.Please try again")
      
   menu()   
    
    
#It will initialize the theatre map when the program starts
def populateTheatreMap():
    rows = 8
    columns = 10
    theatreList = []
    tempList = []
    dash  = '---'
    straightDash = '|'
    
    #This loop takes all zeros(0's) into two dimensional array
    for row in range(rows):
        for column in range(columns):
            tempList.append(0)
        theatreList = tempList.copy()
        theatreListArray.append(theatreList)
        tempList.clear()

#This method will print the theatre map
def printTheatreMap():
   for i in range(8):
      print(theatreListArray[i],'\n')

   menu()

#This method will print the total number of seats booked  in the theatre
def totalBooked(theatreListArray):
   rows = 8
   columns = 10
   seatsBookedCount = 0

   for row in range(rows):
      for column in range(columns):
         if(theatreListArray[row][column]!=0):     #It will enter inside if seats are not empty which means it should not be 0
            seatsBookedCount+=1

   print("the total number of seats reserved in the theatre is ",seatsBookedCount)
   menu()

#This method will remove the empty seats from the row        
def removeEmptySeatsRow(theatreListArray,rowToRemoveEmptySets):
   rows = 8
   columns = 10

   tempList = theatreListArray[rowToRemoveEmptySets-1]  
   for column in range(columns):
    for column in range(columns):
      if(tempList[column] == 0):
         del tempList[column]    #deleting the list item if there is 0 
         tempList.append(0)      #appending 0 to the end after deleting the list item

   menu()
      
   

main()
