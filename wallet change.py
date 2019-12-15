import math

def main():

    ######### DO NOT CHANGE ###############
    wallet = [2, 0, 1, 1, 2, 3, 5, 4] #number of each coin in your wallet
    names = ("$20 Bill", "$10 Bill", "$5 Bill", "Toonies", "Loonies", "Quarters", "Dimes", "Nickles")
    values = (20, 10, 5, 2, 1, 0.25, 0.1, 0.05) #values of each bill/coin
    ########################################

    choice = printMenu()
    
    while(choice != 6):
        if choice == 1:
            displayWalletContents(wallet, names)
        elif choice == 2:
            #TODO: Prompt user for name of coin/bill and save in coinName
            coinName=input("Please enter the coin/bill name: ")
            #TODO: Prompt use for number of coins/bills and save in numOfBillsCoins
            numBillsCoins = int(input("Please enter the number of coins/bills: "))
            addToWallet(wallet, names, coinName, numBillsCoins)
            print("Your updated wallet is ",wallet)
        elif choice == 3:
            #TODO: Prompt user for name of coin/bill and save in coinName
            coinName=input("Please enter the coin/bill name: ")
            #TODO: Prompt use for number of coins/bills and save in numOfBillsCoins
            numBillsCoins = int(input("Please enter the number of coins/bills: "))
            subtractFromWallet(wallet, names, coinName, numBillsCoins)
        elif choice == 4:
            print("Sum of wallet content is ",sumWalletContents(wallet,values))
        elif choice == 5:
            ##TODO: Prompt use for cost of item###
            cost = float(input("Please enter the cost of the item: "))
            purchaseItem(wallet,values,cost)
        choice = printMenu()
        
#TODO: QUESTION 01
def printMenu():
    print("**********")
    print("MENU")
    print("**********")
    print("1. Display wallet contents")
    print("2. Add to wallet")
    print("3. Subtract from wallet")
    print("4. Sum wallet contents")
    print("5. Buy item")
    print("6. Exit application")

    selection = int(input("Please enter your selection: "))
    while(selection<1 or selection >5):
        selection = int(input("Please enter numbers between 1 and 5: "))
    
    return selection

#TODO: QUESTION 02
def displayWalletContents(wallet, names):
    if(len(wallet)==len(names)):
        print("\nThe wallet contents are\n")
        for items in range(len(wallet)):
            print(names[items],"@",wallet[items])
        return

#TODO: Question 03 
def addToWallet(wallet, names, coinName, numOfBillsCoins):
    if(coinName in names):
       wallet[names.index(coinName)]=wallet[names.index(coinName)]+numOfBillsCoins
    return

#TODO: Question 04
def subtractFromWallet(wallet, names, coinName, numOfBillsCoins):
    if(coinName in names):
       if(wallet[names.index(coinName)]-numOfBillsCoins)<0:
           print("Do not update wallet!!!!You do not have numOfBillSCoins coinName in your wallet")
       else:
          wallet[names.index(coinName)] = wallet[names.index(coinName)]-numOfBillsCoins  
    return

#TODO: Question 05
def sumWalletContents(wallet, values):
    sumOfWalletValues = 0
    for walletContents in range(len(wallet)):
        sumOfWalletValues = sumOfWalletValues + values[walletContents]*wallet[walletContents]
    return sumOfWalletValues

#Question 06     
def calculateChange(amountPaid, amountDue):
        values = (20, 10, 5, 2, 1, 0.25, 0.1, 0.05)
        change = [0, 0, 0, 0, 0, 0, 0, 0]
        difference = round(amountPaid - amountDue, 2)
        
        #This loops will check from the highest amount
        while(difference>=20):  
            difference,change = twentyDollarChange(difference,change)
        while(difference>=0 and difference>=10):
            difference,change = tenDollarChange(difference,change)
        while(difference>=0 and difference>=5):
            difference,change = fiveDollarChange(difference,change)
        while(difference>=0 and difference>=2):
            difference,change = toonyDollarChange(difference,change)
        while(difference>=0 and difference>=1):
            difference,change = loonyDollarChange(difference,change)
        while(difference>=0 and difference>=0.25):
            difference,change = quarterDollarChange(difference,change)
        while(difference>=0 and difference>=0.1):
            difference,change = dimesDollarChange(difference,change)
        while(difference>=0 and difference>=0.05):
            difference,change = nicklesDollarChange(difference,change)
        return change
        
    

#It will return updated difference and updated change list
def twentyDollarChange(difference,change):
    change[0]=change[0]+math.floor(difference/20)
    return (difference%20),change

def tenDollarChange(difference,change):
    change[1]=change[1]+math.floor(difference/10)
    return (difference%10),change

def fiveDollarChange(difference,change):
    change[2]=change[2]+math.floor(difference/5)
    return (difference%5),change

def toonyDollarChange(difference,change):
    difference = difference-2
    change[3]=change[3]+math.floor(difference/2)
    return (difference%2),change

def loonyDollarChange(difference,change):
    difference = difference-1
    change[4]=change[4]+math.floor(difference/1)
    return (difference%1),change

def quarterDollarChange(difference,change):
    difference = difference-0.25
    change[5]=change[5]+math.floor(difference/0.25)
    return (difference%0.25),change

def dimesDollarChange(difference,change):
    difference = difference-0.1
    change[6]=change[6]+math.floor(difference/0.1)
    return (difference%0.1),change

def nicklesDollarChange(difference,change):
    difference = difference-0.05
    change[7]=change[7]+math.floor(difference/0.05)
    return (difference%0.05),change
    

    #TODO: COMPLETE the calculate change function to update
    #the change list to include the change recieved.
    #HINT: Start from index 0 
        
    return change

#TODO: Question 07
def purchaseItem(wallet,values, cost):
    #checking if there is enough money in the wallet
    if(sumWalletContents(wallet,values)>=cost):
        if(cost>20):
            twentyCounts = cost/20
        else:
            twentyCounts = 1
            
        #updating wallet by removing 20$ bills
        if(wallet[0]>=twentyCounts):
            wallet[0] = wallet[0]- twentyCounts
            amountPaid = 20*5+0.50  #please change value here if you want to any other amount
            print("You have paid ",amountPaid)
            returnedChange = calculateChange(amountPaid,cost) #It will give the change after taking paidamount and cost
            print("Returned  change is ",returnedChange)
            print("Your wallet before adding change is",wallet)
            for index in range(len(returnedChange)):  #It will add the returned change to the wallet
                wallet[index]=wallet[index]+returnedChange[index]
            print("Your updated wallet after adding change is ",wallet)
            
        else:
            print("You do not have enough twenty dollar amount to pay using twenty dollars.Please give lower amount as cost")
            
        
        
    else:
        print("You do not have enough money in your wallet to buy the item")
    return

#COMPLETED: rounds amount to nearest nickle
def nearestNickle(amount):
    return round(round(amount / 0.05) * 0.05, 2)



main()
