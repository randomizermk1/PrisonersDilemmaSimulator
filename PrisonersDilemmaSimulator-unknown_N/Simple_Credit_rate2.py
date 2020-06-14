# 1 = collude
# 0 = defect
import random


def name():
	return 'Simple_Credit_rate'


opponentMove = 0
opponentHistory = [opponentMove]


def play(opponentMove):
	if opponentMove == 'start':
		return 1


def play(myMove):
	if myMove: return 1
	myhistory = [myMove]
	average = sum(opponentHistory) / len(opponentHistory)
	val = random.randint(0, 1000000)
	if average >= (val / 1000000):
		return 1
	else:
		return 0
