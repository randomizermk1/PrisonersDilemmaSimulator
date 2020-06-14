import timeit, Always_Collude, Always_Defect, TitForTat, Total_random, randomColluding, randomDefecting, Grim_trigger, \
    pavlov, Simple_Credit_rate, Generous_Credit_rate

strategies = [Always_Collude, Always_Defect, TitForTat, Total_random, randomColluding, randomDefecting, Grim_trigger,
              pavlov, Simple_Credit_rate, Generous_Credit_rate]
Fscores = {}
scores = {}
for s in strategies:
    Fscores[s.name()] = 0


def game(player1, player2, rounds):
    global scores
    p1Score = 0
    p2Score = 0
    p1Move = player1.play('start')
    p2Move = player2.play('start')
    for i in range(rounds):
        if p1Move == 1 and p2Move == 1:
            p1Score += 1
            p2Score += 1

        if p1Move == 1 and p2Move == 0:
            p2Score += 2
            p1Score -= 2

        if p1Move == 0 and p2Move == 1:
            p2Score -= 2
            p1Score += 2

        if p1Move == 0 and p2Move == 0:
            p2Score -= 1
            p1Score -= 1

        prevP1Move = p1Move
        prevP2Move = p2Move
        p1Move = player1.play(prevP2Move)
        p2Move = player2.play(prevP1Move)


    if player1 != player2:
        if p1Score > p2Score:
            return p1Score / int(rounds), p2Score / int(rounds), (player1.name(), 'Beats', player2.name())
        if p2Score > p1Score:
            return p1Score / int(rounds),p2Score / int(rounds), (player1.name(), 'Loses', player2.name())
        if p1Score == p2Score:
            if p1Move == p2Move:
                if (p1Score / int(rounds)) == 1:
                    return p1Score / int(rounds),p2Score / int(rounds), (player1.name(), 'Coops', player2.name())
                if (p1Score / int(rounds)) == -1:
                    return p1Score / int(rounds), p2Score / int(rounds),(player1.name(), 'Defects', player2.name())
                else:
                    return p1Score / int(rounds), p2Score / int(rounds),(player1.name(), 'Balance_out', player2.name())
            else:
                return p1Score / int(rounds), p2Score / int(rounds),(player1.name(), 'Balance_out', player2.name())

    else:
        if p1Score == p2Score and p1Move == p2Move:
            if p1Score < 0:
                return (p1Score + p2Score) / (2 * int(rounds)), p1Score / int(rounds), p2Score / int(rounds), (
                player1.name(), 'Defects', player1.name())
            if p1Score > 0:
                return (p1Score + p2Score) / (2 * int(rounds)), p1Score / int(rounds), p2Score / int(rounds), (
                player1.name(), 'Coops', player1.name())
        else:
            return (p1Score + p2Score) / (2 * int(rounds)), p1Score / int(rounds), p2Score / int(rounds), (
                player1.name(), 'Diverges', player1.name())


def statlist(results):
    if results < 0.005:
        return round(results, 10)
    elif results < 0.05:
        return round(results, 6)
    elif results < 1:
        return round(results, 4)
    else:
        return round(results, 2)


def timer(stop, start):
    if (stop - start) < 0.05:
        print('')
    elif (stop - start) < 2:
        print('processing time', round((stop - start), 4), 'sec')
    elif (stop - start) < 60:
        print('processing time', round((stop - start), 2), 'sec')
    elif ((stop - start) / 60) < 60:
        print('processing time', round(((stop - start) / 60), 1), 'min')
    else:
        print('processing time', round((stop - start) / 60 * 60), 'hrs')


def testStrategy(strategy, rep):
    global opscore, selfscore, start1, x1, x2, E2, E1

    print("--------------------------------------------------------")
    print('P1=', strategy.name())
    print('When N =', rep)
    print(" ")
    for s in strategies:
        start = timeit.default_timer()
        if s != strategy:
            otherS, otherO, x = game(strategy, s, rep)
            Fscores[strategy.name()] += otherS
            opscore = Fscores[strategy.name()] / (len(strategies) - 1)
            a, b, c = x
            print(a, b, 'VS', c)
            if otherS == otherO:
                print('With E(u):', statlist(otherS))
            else:
                print('With P1 E(u):', statlist(otherS), 'P2 E(u):', otherO)

        else:
            selfS, p1, p2, x = game(strategy, s, rep)
            selfscore = selfS
            a, b, c = x
            print(a, b, 'VS', c)
            print('With E(u):', 'p1:', statlist(p1), 'p2:', statlist(p2), )
            print('With AVG:', statlist(selfS))
        stop = timeit.default_timer()
        timer(stop, start)
        print(" ")
    print("E(u) AVG VS others", statlist(opscore))
    print('')
    print('--------------Expected Utility Stat List--------------')
    print(a, "  N:", rep)

    print('')
    print("TotalAVG:", ((opscore * 10) + selfscore) / 11)
    print("VS_self", statlist(selfscore))
    print("VS_OPP", statlist(opscore))

