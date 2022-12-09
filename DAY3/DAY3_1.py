import os

def pullValue(theChar):
	if theChar.isupper():
		return ord(theChar)-38
	else:
		return ord(theChar)-96

curFile = open("input.txt",'r').readlines()
arrayList=[]
tempTotal=0
curMax=0
totalArray=[]
set1=set()
set2=set()
prioritySum=0
for line in curFile:
	arrayList.append(line[:-1])
	
print(arrayList)

for line in arrayList:
	set1=set(line[0:len(line)//2])
	set2=set(line[(len(line)//2):len(line)+1])
	setIntersect=set1.intersection(set2)
	print(set2)
	print(set1)
	print(setIntersect)
	prioritySum +=pullValue(list(setIntersect)[0])
print(prioritySum)