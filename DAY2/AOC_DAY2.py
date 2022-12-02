import os

def checkScore(elfChoice, urChoice):
	score=0
	if urChoice == "X": #rock
		score+=1
		if elfChoice == "A":#rock
			score+=3
		elif elfChoice=="C":#scissors
			score+=6

	elif urChoice=="Y": #paper
		score+=2
		if elfChoice == "A":#rock
			score+=6
		elif elfChoice=="B":#paper
			score+=3
			
	elif urChoice=="Z": #scissors
		score+=3
		if elfChoice=="B":#paper
			score+=6
		elif elfChoice=="C":#scissors
			score+=3
	return score
			

score=0
myfile = open("input.txt", "r")
myline = myfile.readline()
myArr=[]
while myline:
    myArr.append(myline[:-1])
    myline = myfile.readline()
    tempArr= myArr[-1].split(" ")
    score+=checkScore(tempArr[0],tempArr[1])
myfile.close()

print(score)