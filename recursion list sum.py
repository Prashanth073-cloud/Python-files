#Name: Prashanth Chintala
#CNumber: C0759844
#Date: 12-04-2019
#Question: Q5

def main():
  numbersList = [10,5,7,9,8,7] #list values
  listSumValue = recursiveListSum(numbersList) #It will call the recursiveListMethod and store the result in listSumValue
  print("Sum of list values of",numbersList,"is",listSumValue) 


#This method will call itself until it sums the total elements in the list
def recursiveListSum(numbersList):
    if(len(numbersList)== 1):  #this condition will check whether if there is only one value in list.If one value is present it will return its value
        return numbersList[0]
    else:
        return numbersList[len(numbersList)-1]+recursiveListSum(numbersList[:len(numbersList)-1]) #this will sum the last element with the returned element

main()
