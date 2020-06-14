# 1 = collude
# 0 = defect
import random


def name():
    return 'Generous_Credit_rate'




def play(opponentMove):
    opponentHistory = []
    opponentHistory.append(opponentMove)
    myhistory = []
    if opponentMove == 'start':
        myhistory.append(1)
        return 1
    else:
        val = random.randint(1, (len(myhistory) + len(opponentHistory)))
        if val <= sum(opponentHistory) + sum(myhistory):
            myhistory.append(1)
            return 1
        else:
            return 0

    # average = sum(opponentHistory) + sum(myhistory)/(len(myhistory) + len(opponentHistory))
