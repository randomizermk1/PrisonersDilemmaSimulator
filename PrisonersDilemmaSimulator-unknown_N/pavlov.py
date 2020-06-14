import random


# 1 = collude
# 0 = defect

def play(opponentMove):
    opponentHistory = []
    myHistory = []
    if opponentMove == 'start':
        myHistory.append(1)
        return 1
    opponentHistory.append(opponentMove)
    if opponentHistory[-1] == 1:
        myHistory.append(1)
        return myHistory[-1]
    else:
        return random.randint(0, 1)


def name():
    return 'pavlov'
