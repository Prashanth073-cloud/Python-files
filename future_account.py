#Name:Prashanth Chintala,CNumber:C0759844,Question:Q19,Date:11/05/2019

#Initializing variables
futureValue = 0
presentAccountValue = 0
monthlyIntRate = 0
noOfMonths = 0

#main() function
def main():
    presentAccountValue,monthlyIntRate,noOfMonths = get_inputs()                #getting inputs from the get_inputs() functions
    futureValue = calculate_futureValue(presentAccountValue,monthlyIntRate,noOfMonths) #calculating future value from the calculate_futureValue function
    print("The future value of your account is ",format(futureValue,'.2f'))


#This function takes inputs from the user and returns to main function
def get_inputs():
    presentAccountValue = float(input("Please enter your Present Account Value "))
    monthlyIntRate = float(input("Please enter your monthly interest rate "))
    noOfMonths = float(input("Please enter the number of months that money will be left in the account "))
    return presentAccountValue,monthlyIntRate,noOfMonths


#This function calculates future account value and returns it to main funtion
def calculate_futureValue(presentAccountValue,monthlyIntRate,noOfMonths):
    futureValue = presentAccountValue * (1+monthlyIntRate/100)**noOfMonths
    return futureValue

#Calling main function when the program starts
main()
