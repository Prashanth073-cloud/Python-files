def main():
 unsortedList = [12,11,13,5,6,8,1,78,52]
 unsortedList = selectionSort(unsortedList)
 print("result is ",unsortedList)



    
def selectionSort(unsortedList):
    for i in range(len(unsortedList)):
       j = i+1
       if(j<=len(unsortedList)):
        temp = unsortedList[i]
        for f in range(j):
            if(unsortedList[f]>unsortedList[i]):
                unsortedList[i]=unsortedList[f]
                unsortedList[f]=temp
                temp = unsortedList[i]
        print(unsortedList)
    return unsortedList
            
main()    
