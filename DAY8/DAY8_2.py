curFile = open("input.txt",'r').readlines()
arrayList=[]
orchArray=[]

##################################
#		|Assignments|			 #
##################################
for line in curFile:			 #
	arrayList.append(line[:-1])	 #
								 #
for line in arrayList:			 #
	orchArray.append([*line])	 #
								 #
##################################
counter=0
maxScore=0
rightCount=0
leftCount=0
upCount=0
downCount=0

for row in range(1,len(orchArray)-1):
	for column in range(1,len(orchArray)-1):
		currentHeight=int(orchArray[row][column])

		#UP FROM IT
		for i in range(row-1,-1,-1):
			upCount+=1
			if not (int(orchArray[i][column]) < currentHeight):
				break

		#DOWN FROM IT
		for i in range(row+1,len(orchArray)):
			downCount+=1
			if not (int(orchArray[i][column]) < currentHeight):
				break

		#RIGHT FROM IT (CHECK)
		for i in range(column+1,len(orchArray)):
			rightCount+=1
			if not (int(orchArray[row][i]) < currentHeight):
				break

		#LEFT FROM IT
		for i in range(column-1,-1,-1):
			leftCount+=1
			if not (int(orchArray[row][i]) < currentHeight):
				break

		tempScore = leftCount*rightCount*upCount*downCount
		if tempScore > maxScore:
			maxScore=tempScore
		rightCount=0
		leftCount=0
		upCount=0
		downCount=0

print(maxScore)