# 1 = collude
# 0 = defect
import random


def name():
    return 'Simple_Credit_rate'


def play(opponentMove):
    opponentHistory = []
    if opponentMove == 'start':
        return 1
    else:
        opponentHistory.append(opponentMove)
    average = sum(opponentHistory) / len(opponentHistory)
    val = random.randint(0, 1000000)
    if average >= (val / 1000000):
        return 1
    else:
        return 0
