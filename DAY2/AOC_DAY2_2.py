import os

def checkScore(elfChoice, urChoice):
	score=0
	if urChoice == "X": #lose
		score+=0
		if elfChoice == "A":#rock
			score+=3
		elif elfChoice=="B":#paper
			score+=1
		elif elfChoice=="C":#scissors
			score+=2

	elif urChoice=="Y": #draw
		score+=3
		if elfChoice == "A":#rock
			score+=1
		elif elfChoice=="B":#paper
			score+=2
		elif elfChoice=="C":#scissors
			score+=3
	elif urChoice=="Z": #win
		score+=6
		if elfChoice == "A":#rock
			score+=2
		elif elfChoice=="B":#paper
			score+=3
		elif elfChoice=="C":#scissors
			score+=1
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