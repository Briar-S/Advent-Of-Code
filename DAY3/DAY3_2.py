import os

def pullValue(theChar):
	if theChar.isupper():
		return ord(theChar)-38
	else:
		return ord(theChar)-96

curFile = open("input.txt",'r').readlines()
arrayList=[]
set1=set()
set2=set()
set3=set()
prioritySum=0
counter=0;

for line in curFile:
	arrayList.append(line[:-1])
	
print(arrayList)

for line in arrayList:
	if counter==0:
		set1=set(line[:])
		counter+=1
	elif counter==1:
		set2=set(line[:])
		counter+=1
	elif counter==2:
		set3=set(line[:])
		setIntersect=set1.intersection(set2)
		setIntersect=setIntersect.intersection(set3)
		print(setIntersect)
		prioritySum +=pullValue(list(setIntersect)[0])
		counter=0
print(prioritySum)