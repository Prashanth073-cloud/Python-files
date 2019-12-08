#Name:Prashanth Chintala
#CNumber: C0759844
#Date: 12-04-2019
#Question:Q2


def main():
    x = int(input("Please enter the x value: "))
    y = int(input("Please enter the y value: "))
    result = multiplication(x,y)  #This method will call the multiplication function
    #print(str(x)+"*"+str(y)+str("=")+result) #It will print the final result after the recursion is completed
    print("Multplication of ",x,"and",y,"is",result)



#This method calls itself x times and then returns to the main().It will print output like this 7*4=4+4+4+4+4+4+4
#def multiplication(x,y):
 #   count=0
  #  global multiplicationResult
   # if(x==1):  
    #    return y
    #else:
       #return str(y)+str("+")+str(multiplication(x-1,y))


#This method calls itself x times and then returns to the main()
def multiplication(x,y):
    global multiplicationResult
    if(x==1):  
        return y
    else:
       return y+multiplication(x-1,y) #calling mutiplication(x,y) until x==1
        

    

main()
    
