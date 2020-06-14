# Code based on Sanjin Dedic's PD sim, creator of Robotix.com.au
# Watch YouTube Explanation Here: https://youtu.be/pMHOqotUiP8
# --------------------------------------------------------
# Heavily modified and Recreated by Randomizer
# randomizer@hanyang.ac.kr

import AIsimulation
import AIsimulation_log
import AIsimulation_log_sum
import timeit
import Always_Collude
import Always_Defect
import Grim_trigger
import Simple_Credit_rate
import Generous_Credit_rate
import pavlov
import Total_random
import randomColluding
import randomDefecting
import TitForTat

print(" ")
print("Prisoner's Dilemma Simulator")
print("By randomizer: randomizer@hanyang.ac.kr")
print("Ver_1.4")
print(" ")
print(" ")
print("Payoff Matrix")
print(" ")
print("--------------------------------------------------------")


def timer(stop, start):
    if (stop - start) < 3:
        print('Total processing time', round((stop - start), 5), 'sec')
    elif (stop - start) < 60:
        print('Total processing time', round((stop - start), 2), 'sec')
    elif ((stop - start) / 60) < 60:
        print('Total processing time', round(((stop - start) / 60), 1), 'min')
    else:
        print('Total processing time', round((stop - start) / 60 * 60), 'hrs')


def print_table(table):
    col_width = [max(len(x) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")


mylist = [(' ', 'P1_Collude', 'P1_Defect'), ('P2_Collude', '+1 / +1 (Coop)', '-2 / +2 (Lose/Win)'),
          ('P2_Defect', '+2 / -2 (Win/Lose)', '-1 / -1 (Defects)')]

table = [tuple(x) for x in mylist]
print_table(table)
print("--------------------------------------------------------")
print(" ")
print('If "P1_Score" = "P2_Score" but do not "Coop" or "Defect",')
print('Then it "Balance_out"')
print(" ")
def sim(choice):
    if choice == 1:
        print("--------------------------------------------------------")
        if log == "1":
            print('Total Logging enabled')
        if log == "2":
            print('Summary Logging enabled')
        else:
            print('Logging disabled')
        print(" ")
        print('here are the strategies, choose one')
        print(" ")
        print(choices1)
        print(choices2)
        print(choices3)
        print(" ")
        print("Custom_Made_Strategies")
        print(choices4)
        print(" ")
        num = int(input('choose a strategy via number :'))
        strategy = strategies[num]
        print(" ")
        print('Amount of repetitions (multiplies by 1000)')
        repeater = int(input('choose repeats via number:'))
        start1 = timeit.default_timer()
        if log == '1':
            AIsimulation_log.testStrategy(strategy, repeater * 1000)
        if log == '2':
            AIsimulation_log_sum.testStrategy(strategy, repeater * 1000)
        else:
            AIsimulation.testStrategy(strategy, repeater * 1000)
        choice = 0
        stop1 = timeit.default_timer()
        if log == "1":
            print('Printing Results Via CSV...')
        timer(stop1, start1)
    print(" ")
    choice = int(input('press 1 to repeat'))
    print(" ")

while True:
    choices1 = ['1-Always_Collude', '2-Always_Defect', '3-TitForTat']
    choices2 = ['4-Total_random', '5-randomColluding']
    choices3 = ['6-randomDefecting', '7-Grim_trigger', '8-pavlov']
    choices4 = ['9-Simple_Credit_rate', '10-Generous_Credit_rate']
    strategies = {1: Always_Collude, 2: Always_Defect, 3: TitForTat, 4: Total_random, 5: randomColluding,
                  6: randomDefecting,
                  7: Grim_trigger, 8: pavlov, 9: Simple_Credit_rate, 10: Generous_Credit_rate}
    print('press 1 to log entire results')
    print('press 2 to log only summarized results')
    log = input('Press any other key to disregard: ')
    choice = 1
    sim(choice)

    from importlib import reload

    timeit = reload(timeit)
    AIsimulation = reload(AIsimulation)
    Simple_Credit_rate = reload(Simple_Credit_rate)
    Generous_Credit_rate = reload(Generous_Credit_rate)
    Always_Collude = reload(Always_Collude)
    Always_Defect = reload(Always_Defect)
    Grim_trigger = reload(Grim_trigger)
    Total_random = reload(Total_random)
    randomColluding = reload(randomColluding)
    randomDefecting = reload(randomDefecting)
    TitForTat = reload(TitForTat)
    pavlov = reload(pavlov)

    if choice != 1:
        print('-------------- Simulation_Terminated --------------')
        break
