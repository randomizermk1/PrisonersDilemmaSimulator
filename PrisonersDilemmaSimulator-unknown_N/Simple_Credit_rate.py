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
    val = random.randint(1, len(opponentHistory))
    if val <= sum(opponentHistory):
        return 1
    else:
        return 0
