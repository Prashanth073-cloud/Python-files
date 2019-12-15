students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


#printing students in sorting order of their scores
def greater(students):
    return students[1]
students.sort(key=greater)
print(students)

student1=students[0]
student2=students[1]
#getting student lowest grade
if(student1[1]!=student2[1]):
    print("Second lowest grade is ",student2)
    secondLowestGrade = student2[1]

counter = 0
final2DList=[]
#finding if there are any repeated second lowest grades and if present,storing in to the list
for items in range(len(students)):
    student = students[items]
    tempList=[]
    if(student[1]==secondLowestGrade):
        tempList.append(student[0])
        tempList.append(student[1])
        normalList = tempList.copy()
        final2DList.append(normalList)
        tempList.clear()
final2DList.sort()
print(final2DList)


