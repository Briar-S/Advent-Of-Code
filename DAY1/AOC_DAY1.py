import os

curFile = open("input.txt",'r').readlines()
arrayList=[]
tempTotal=0
curMax=0
totalArray=[]

for line in curFile:
	size = len(line)
	arrayList.append(line[:-1])

for line in arrayList:
	if line != "":
		tempTotal+=int(line)
	else:
		totalArray.append(tempTotal)
		if tempTotal > curMax:
			curMax=tempTotal
		tempTotal=0
	
totalArray.sort()
print(totalArray)