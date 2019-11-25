#Name: Prashanth Chintala
#CNumber: C0759844
#Date: 11/18/2019
#Question: 11


def main():
    
    userName = input("Please enter your name: ")    #Asking for user input
    userDescription = input("Please describe about yourself: ") #Asking user to describe about themselves

    filePointer = open("userDetails.html","w")  #opening the file
    filePointer.write("<html>\n<head>\n<title>User Details</title>\n</head>\n<body>\n<center>\n<h1>"+userName+"</h1>\n</center>\n<hr>\n"+userDescription+"</hr>\n</body>\n</html>") #writing html content to file
    filePointer.close()     #closing the file



main()
