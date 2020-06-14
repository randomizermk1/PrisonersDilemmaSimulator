# 1 = collude
# 0 = defect

import random


def roll():
    val = random.randint(1, 5)
    if val > 2:
        return 1
    else:
        return 0


def play(opponentMove):
    if opponentMove == 'start':
        return roll()
    return roll()


def name():
    return 'randomColluding'
