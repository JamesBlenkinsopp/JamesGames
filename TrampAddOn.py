#tramp game prog
import random

#modifiers: grouped easy-med-hard-custom(expert)
skillsIn = [["(no twist)","1/2 twist "],["1/1 twist "],["3/2 twist "],["2/1 twist "]]
#skillsOut = [[" 1/2 to feet"],[" 1/1 to feet"],[" 3/2 to feet"]] #probs dont need, seperate skill
skillsOut = [["jump","to seat drop"],["to front drop","to back drop"],[],[]]
#follow a skill out i.e. back into pullover
#have back tag to allow to string to back
followSkills = [["to feet"],["pullover to feet"],["pullover to back","turnover to back","ballout"],["pullover 1/1 to ft","pullover 1/2 to ft"]]
shapes = [["tuck ","pike ","straddle "],[],["straight "],["puck "]]
skillShaped = [["jump"],["front drop","forward turn over"],["front somi","back somi","barani"],[]]
skills = [[],[],["crash dive"],["full","rudi"]]
backSkills=["to back drop","pullover to back","turnover to back","forward turn over","crash dive"]

#code
print("welcome to automised add on")
difficulty = input("select difficulty: e/m/h/x ")
inp = input("custom rules? y/n ")
if inp== "y":
	cont = True
	inpArr=[]
	while cont == True:
		trick = input("input custom skill: ")
		inpArr.append(trick)
		inp = input("does this land on your back? y/n ")
		if inp == "y":
			backSkills.append(trick)
		inp = input("more? y/n ")
		if inp == "n":
			cont = False
	if difficulty =="e":
		skills[0]=skills[0]+inpArr
	elif difficulty =="m":
		skills[1]=skills[1]+inpArr
	elif difficulty =="h":
		skills[2]=skills[2]+inpArr
	else:
		skills[3]=skills[3]+inpArr

#game start
print("game start! heres the standalone skills youre playing with: ")
#moves is total list to pull from, sorted by skills, shaped skills, shapes, moves in, out, back drop skills
moves = [[],[],[],[],[],[]]
if difficulty =="e":
	lim = 1
elif difficulty =="m":
	lim = 2
elif difficulty =="h":
	lim = 3
else:
	lim = len(skills)
for m in range(0,lim):
	for n in range(len(skills[m])):
		print(skills[m][n])
		moves[0].append(skills[m][n])
print("")
print("the following skills can have a specified shape: ")
for m in range(lim):
	for n in range(len(skillShaped[m])):
		print(skillShaped[m][n])
		moves[1].append(skillShaped[m][n])
print("")
print("these possible shapes for skills are: ")
for m in range(lim):
	for n in range(len(shapes[m])):
		print(shapes[m][n])
		moves[2].append(shapes[m][n])
print("")
print("as well as combinations of: ")
for m in range(lim):
	for n in range(len(skillsIn[m])):
		print(skillsIn[m][n])
		moves[3].append(skillsIn[m][n])
print("")
print("into:")
for m in range(lim):
	for n in range(len(skillsOut[m])):
		print(skillsOut[m][n])
		moves[4].append(skillsOut[m][n])
print("")
print("and back landing skills can be followed by:")
for m in range(lim):
	for n in range(len(followSkills[m])):
		print(followSkills[m][n])
		moves[5].append(followSkills[m][n])
print("")
print("")

names=[]
cont = True
while cont == True:
	names.append(input("enter player name: "))
	inp = input("more players? y/n ")
	if inp == "n":
		cont=False
print("players are: ")
for m in range(len(names)):
	print(names[m])
random.shuffle(names)
#mix order
#pointer for whose go it is
namePointer = 0
#current move list
routine = ["start"]
#to ensure move arrays not empty causing errors
for m in range(len(moves)):
	if moves[m]==[]:
		moves[m].append("straight jump")
print("when players fail, they will be removed")

while len(names)>1:#while no winner
	print(names[namePointer]+"'s go!")
	if routine[len(routine)-1] in (moves[4]+ moves[5]) and routine[len(routine)-1] not in (backSkills+["to feet","jump","straight jump"]): #not feet land/back - not regular or back skill

		randVal = 3
		newMove = moves[randVal][random.randint(0,len(moves[randVal])-1)]+"to feet"

	elif routine[len(routine)-1] in (backSkills): #back land - not regular skill
		randVal = random.choice([3,5])
		newMove = moves[randVal][random.randint(0,len(moves[randVal])-1)]
		if randVal == 3:
			newMove=newMove+random.choice(moves[4])

	else: #feet - not back skill
		randVal = random.choice([0,2,3])
		newMove = moves[randVal][random.randint(0,len(moves[randVal])-1)]
		if randVal == 2:
			newMove=newMove+random.choice(moves[1])
		if randVal == 3:
			newMove=newMove+random.choice(moves[4])

	routine.append(newMove)
	print("the next move is "+newMove)
	print("")
	print("the full routine is: ")
	for n in range(len(routine)):
		print(routine[n])
	print("")
	inp = input("did "+names[namePointer]+" do it? y/n ")
	if inp == "y":
		namePointer=namePointer+1
	elif inp == "n":
		names.pop(namePointer)
	if namePointer >=len(names):
			namePointer =0

print("the winner is... "+names[0])

#todo
#make highest level more likely
#fix body landings to include (optional twist) to feet
#use file for storing custom moves
#gui?
