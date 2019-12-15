scores = [2,3,6,6,5]
sampleList = list(dict.fromkeys(scores))
sampleList.sort(reverse=True)
print(sampleList)

if 6 in scores:
    print("6")
else:
    print("No")
