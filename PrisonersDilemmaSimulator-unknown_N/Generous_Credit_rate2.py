# 1 = collude
# 0 = defect
import random


def name():
    return 'Generous_Credit_rate'


opponentMove = 0


def play(opponentMove):
    if opponentMove == 'start':
        return 1


opponentHistory = [opponentMove]


def play(myMove):
    if myMove: return 1
    myhistory = [myMove]
    average = sum(opponentHistory) + sum(myhistory)/(len(myhistory) + len(opponentHistory))
    val = random.randint(0, 100000)
    if average >= (val/100000):
        return 1
    else:
        return 0
