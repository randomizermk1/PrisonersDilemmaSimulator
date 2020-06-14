import alwaysCollude, alwaysDefect, titForTat, randomBasic, randomColluding, randomDefecting, grudger, pavlov, Sanjin, \
	myStrategy, myStrategy2

strategies = [alwaysCollude, alwaysDefect, titForTat, randomBasic, randomColluding, randomDefecting, grudger, pavlov,
              Sanjin, myStrategy, myStrategy2]


def play(AI, rounds):
	print('Hello human what is your name?')
	yourName = input()
	print('Human game against', AI.name())
	global scores
	yourScore = 0
	AIscore = 0

	print('type 1 to collude and type 0 to defect')
	yourMove = int(input())
	AImove = AI.play('start')

	for i in range(rounds):
		if yourMove == 1 and AImove == 1:
			yourScore += 1
			AIscore += 1
			print('it was a draw')
		elif yourMove == 1 and AImove == 0:
			AIscore += 2
			print(AI.name(), 'defected and won')
		elif yourMove == 0 and AImove == 1:
			yourScore += 2
			print('you defected and won')
		else:
			print('you both defected')
		print('type 1 to collude and type 0 to defect')
		yourPrevMove = yourMove
		yourMove = int(input())
		AImove = AI.play(yourPrevMove)
	if yourScore > AIscore:
		print(yourName, 'beats', AI.name(), yourScore, '-', AIscore)
	elif AIscore > yourScore:
		print(AI.name(), 'beats', yourName, AIscore, '-', yourScore)
	else:
		print('it was a draw', yourName, yourScore, AI.name(), AIscore)
