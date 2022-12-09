import os

def range_subset(range11,range12, range21,range22):
    if range11>range22 or range12<range21:
    	return False
    return True

curFile = open("input.txt",'r').readlines()
arrayList=[]
counter=0
i=0
for line in curFile:
	arrayList.append(line[:-1])

for line in arrayList:
	ranges=line.split(',')
	ranges1=ranges[0].split('-')
	ranges2=ranges[1].split('-')
	range11=int(ranges1[0])
	range12=int(ranges1[1])
	range21=int(ranges2[0])
	range22=int(ranges2[1])
	print('================')
	print(str(range11) + ":" + str(range12))
	print(str(range21) + ":" + str(range22))
	
	if(range_subset(range11,range12,range21,range22)):
		print("+1")
		counter+=1
	print('================')
print(counter)

#for line in arrayList: