def main():
 unsortedList = [12,11,13,5,6]
 unsortedList = selectionSort(unsortedList)
 print(unsortedList)




def selectionSort(unsortedList):
    for i in range(len(unsortedList)):
        temp = unsortedList[i]
        for j in range(i+1,len(unsortedList)):
            #print(i,j)
            if(unsortedList[j]<unsortedList[i]):
                unsortedList[i]=unsortedList[j]
                unsortedList[j]=temp
                temp = unsortedList[i]
        print(unsortedList)
    return unsortedList
            
main()    
