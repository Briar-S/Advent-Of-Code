import os

stack=[]
stack.append(["C","Z","N","B","M","W","Q","V"])
stack.append(["H","Z","R","W","C","B"])
stack.append(["F","Q","R","J"])
stack.append(["Z","S","W","H","F","N","M","T"])
stack.append(["G","F","W","L","N","Q","P"])
stack.append(["L","P","W"])
stack.append(["V","B","D","R","G","C","Q","J"])
stack.append(["Z","Q","N","B","W"])
stack.append(["H","L","F","C","G","T","J"])
tasks=[]

curFile = open("input.txt",'r').readlines()
arrayList=[]
for line in curFile:
	arrayList.append(line[:-1])

for line in arrayList:
	tasks.append(line.split(','))

for task in tasks:
	for i in range(0,int(task[0])):
		fromThis=int(task[1])-1
		toThis=int(task[2])-1
		stack[toThis].append(stack[fromThis].pop(-(int(task[0])-i)))

for thing in stack:
	print(thing[-1])