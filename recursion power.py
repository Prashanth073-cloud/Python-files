#Name: Prashanth Chintala
#CNumber: C0759844
#Date: 12-04-2019
#Question: Q7

def main():
 number = int(input("Please eneter the number to be raised: "))
 exponent = int(input("Please enter the exponent: "))
 result = recursivePower(number,exponent)
 print(number,"raised by",exponent,"times is",result) #printing result
 


def recursivePower(number,exponent):
    if(exponent == 0):
        return 1
    else:
        return number * recursivePower(number,exponent-1) #calling the same method until exponent becomes 0

main()
