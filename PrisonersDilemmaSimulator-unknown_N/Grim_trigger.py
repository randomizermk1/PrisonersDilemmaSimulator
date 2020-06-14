# 1 = collude
# 0 = defect

beNice = True


def play(opponentMove):
	opponentHistory = []
	global beNice
	opponentHistory.append(opponentMove)
	if opponentMove == 'start':
		beNice = True
		opponentHistory.append(1)
		return 1
	if opponentHistory[-1] == 0:  # this refers to the last move
		beNice = False

	if beNice == True:
		return 1
	else:
		return 0


def name():
	return 'Grim_trigger'
