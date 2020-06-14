# 1 = collude
# 0 = defect

import random


def play(opponentMove):
    if opponentMove == 'start':
        return random.randint(0, 1)
    return random.randint(0, 1)


def name():
    return 'Total_random'
