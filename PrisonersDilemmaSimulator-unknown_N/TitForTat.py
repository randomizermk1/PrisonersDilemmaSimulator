# 1 = collude
# 0 = defect

def play(opponentMove):
    opponentHistory = [opponentMove]
    if opponentMove == 'start':
        return 1
    else:
        if opponentHistory:
            return opponentHistory[-1]


def name():
    return 'TitForTat'
