curFile = open("input.txt",'r').readline()
splitarray=[*curFile]
splitarray.pop()

leftItr=0
rightItr=13
for i in range(0,len(splitarray)):
	tempList=splitarray[leftItr+i:rightItr+1+i]
	tempSet=set(tempList)
	if(len(tempSet)==14):
		print(rightItr+1+i)
		break;