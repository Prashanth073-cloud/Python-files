def main():
     print("This question is from HackerRank\n")
     minionGame("BANANA")
     


def minionGame(name):
    stuartCounter =0
    print("possible combinations of constants by Stuart")
    for letter in range(len(name)):
        savedLetter = ""
        if((name[letter]!="A" and name[letter]!="E" and name[letter]!="I" and name[letter]!="O" and name[letter]!="U") and letter+1<=len(name)):
            for letters in range(letter,len(name)):
                savedLetter = savedLetter+name[letters]
                print(savedLetter)
                stuartCounter+=1
    #print(rowCounter)

    kevinCounter =0
    print("possible combinations of vowels by Kevin")
    for letter in range(len(name)):
        savedLetter = ""
        if((name[letter]=="A" or name[letter]=="E" or name[letter]=="I" or name[letter]=="O" and name[letter]=="U") and letter+1<=len(name)):
            for letters in range(letter,len(name)):
                savedLetter = savedLetter+name[letters]
                print(savedLetter)
                kevinCounter+=1
    #print(kevinCounter)

    if(kevinCounter>stuartCounter):
        print("Kevin",kevinCounter)
    else:
        print("Stuart",stuartCounter)
            
            

main()
    
