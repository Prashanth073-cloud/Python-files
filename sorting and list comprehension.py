import math

#Assignment 09 - Python Sorting and List Comprehension

#Your Name: Prashanth Chintala
#Your C#: C0759844
#Date: 12-03-2019

##### PART A - Sorting: #####

#Q1. Use Python's list.sort() method to sort numbers1to10 in reverse order
numbers1to10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1to10.sort(reverse=True)
print("Reverse sort of numbers are ",numbers1to10,"\n")

#Q2. Use Python's list.sort() method to sort the list in case-insensitive 
#    alphabetical order.
#Hint: Look at the example in the Google Developer link
studentNames = ["Jake", "aaron", "Ryan", "samantha", "nicole"]
studentNames.sort(key=str.casefold)
print("Sorting in alphabetical order ",studentNames,"\n")

#Q3. Use Python's list.sort() method to sort the below (student_name, grade) 
#    tuples by grades in descending order
studentNames = [("Jake", 80),
                ("aaron", 72),
                ("Ryan", 93),
                ("samantha", 68),
                ("nicole", 88)
               ]
def myFn(studentNames):
    return studentNames[1]
studentNames.sort(key=myFn)
print("Sorting grades in descending order are ",studentNames,"\n")



#Q4. Use Python's sorted() function to sort the listStrings[] by LENGTH of the 
#    strings and store the result in the sortedStringsList[]
listStrings = ["zzzz", "ccc", "aa", "bb", "x"]
sortedStringsList = []
sortedStringList = sorted(listStrings,key=len)
print("sorting list using sorted and by its length ",sortedStringList,"\n")

#Q5. Use Python's sorted() function to sort the the listStrings[] by MIDDLE 
#    character in each string.
# HINT: use math.floor() to help identify the middle index. 
listStrings = ["zxzz", "cac", "ba", "ab", "y"]
def sortByMiddle(listStrings):
    return listStrings[math.floor((len(listStrings)-1)/2)]

print("sorting strings by middle character",sorted(listStrings,key=sortByMiddle),"\n")


    
##### PART B - List Comprehension: #####

#Q6. Use list comprehension with range() to populate the below list with all 
#    the integers between 1 and 100, inclusive

numbers1to100 = [integers for integers in range(1,101)]
print("numbers from 1 to 100",numbers1to100,"\n")

#Q7. Use list comprehension and the list numbers1to100[] from Q5 to produce a 
#    list populated with each element from numbers1to100 cubed (power 3).
#    You MUST refrence numbers1to100[] in your answer below!
cubeNumbers = [cube**3 for cube in numbers1to100]
print("cube numbers of 1 to 100 are",cubeNumbers,"\n")
#Q8. Use list comprehension to sum items from numbers1to100[] and cubeNumbers[]
#    and store the resulting value in the list below.

sumNumbers = [numbers1to100[i]+cubeNumbers[i] for i in range(len(numbers1to100))]
print("Sum of two lists",sumNumbers,"\n")

#Q9. Use list comprehension with range() to find all the odd numbers between 1 
#    and 1000, inclusive

oddNumbersBetween1and1000 = [oddNumbers for oddNumbers in range(1,1001) if(oddNumbers%2==1)]
print("odd numbers ",oddNumbersBetween1and1000,"\n")

#Q10. Use list compreshension with range() and isPrime() function below to find
#     all prime numbers between 1 and 1000, inclusive



#NOTE: isPrime is COMPLETED and should not be modified.
def isPrime(num):
    for i in range(2,num):
        if num % 2 == 0:
            return False
    return True

primeNumbersBetween1and1000 = [prime for prime in range(1,1001) if(isPrime(prime))]
print("Prime numbers",primeNumbersBetween1and1000,"\n")
