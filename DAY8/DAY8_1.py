curFile = open("input.txt",'r').readlines()
arrayList=[]
orchArray=[]
resultArray=[]

##################################
#		|Assignments|			 #
##################################
for i in range(0,99):			 #
	resultArray.append([])		 #
	for j in range(0,99):		 #
		resultArray[i].append(0) #
for line in curFile:			 #
	arrayList.append(line[:-1])	 #
								 #
for line in arrayList:			 #
	orchArray.append([*line])	 #
								 #
##################################
totalCounter=392

#ROW CHECK T->B
for i in range(1,len(orchArray)-1):
	tempMax=int(orchArray[i][0])
	for j in range(1,len(orchArray)):
		if(int(orchArray[i][j]) > tempMax):
			tempMax=int(orchArray[i][j])
			resultArray[i][j]=1
#ROW CHECK R->L
for i in range(len(orchArray)-2,0,-1):
	tempMax=int(orchArray[i][98])
	for j in range(len(orchArray)-2,0,-1):
		if(int(orchArray[i][j]) > tempMax):
			tempMax=int(orchArray[i][j])
			resultArray[i][j]=1


#COLUMN CHECK T->B
for i in range(1,len(orchArray)-1):
	tempMax=int(orchArray[0][i])
	for j in range(1,len(orchArray)):
		if(int(orchArray[j][i]) > tempMax):
			tempMax=int(orchArray[j][i])
			resultArray[j][i]=1
#COLUMN CHECK B->T
for i in range(len(orchArray)-2,0,-1):
	tempMax=int(orchArray[98][i])
	for j in range(len(orchArray)-2,0,-1):
		if(int(orchArray[j][i]) > tempMax):
			tempMax=int(orchArray[j][i])
			resultArray[j][i]=1


for line in resultArray:
	totalCounter+=line.count(1)
print(totalCounter)