def main():
    unsortedList = [10,1,5,12,1,18,0,6]
    countingSort(unsortedList)


def countingSort(unsortedList):
    countList = []

    #initializing list with zeroes. count list size is maximum of the unsortlist
    for items in range(max(unsortedList)+1):
        countList.append(0)
    #print(countList)

    #counting occurences of list
    for item in range(len(unsortedList)):
        itemValue = unsortedList[item]
        itemCount = 0
        for j in range(len(unsortedList)):
            if(itemValue==unsortedList[j]):
                itemCount+=1
        countList[itemValue]=itemCount
    #print(countList)

    #adding values side by side
    for item in range(len(countList)):
        if(item>0):
            countList[item]=countList[item]+countList[item-1]
    #print(countList)

    sortedList = []
    for i in range(max(unsortedList)+1):
        sortedList.append(0)
        
    #checking unsorted list items value position in the countlist 
    for items in range(len(unsortedList)):
        itemValue = unsortedList[items]
        #print("unsorted list value ",itemValue)
        position = countList[itemValue]
        #print("count list posiiton",position)
        sortedList[position-1]=itemValue
        
        countList[itemValue]=countList[itemValue]-1
        #print("countList after deduction",countList)
    print(sortedList)

    
        
            


    
main()
