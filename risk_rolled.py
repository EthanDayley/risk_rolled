#!/usr/bin/env python3

'''
This is a program to make rolling the
dice in Risk less annoying.
'''


import random
import webbrowser
import os
import colors


def roll() -> int:
    '''
    This function returns the result of
    a random dice roll.
    '''
    return random.randint(1, 6)


def get_casualties(attacking_dice: int, defending_dice: int) -> tuple:
    '''
    This method returns a tuple of the form
    (attacking_casualties, defending_casualties)
    '''
    attacking_rolls = []
    defending_rolls = []
    for i in range(attacking_dice):
        attacking_rolls.append(roll())
    for i in range(defending_dice):
        defending_rolls.append(roll())
    attacking_casualties = 0
    defending_casualties = 0
    attacking_rolls.sort()
    defending_rolls.sort()
    attacking_rolls.reverse()
    defending_rolls.reverse()
    print(attacking_rolls)
    print(defending_rolls)
    num_comparisons = min(attacking_dice, defending_dice)
    for i in range(num_comparisons):
        if attacking_rolls[i] > defending_rolls[i]:
            defending_casualties += 1
        else:
            attacking_casualties += 1
    return (attacking_casualties, defending_casualties)


def get_int_in_bounds(msg: str, lower_bound: int, upper_bound: int) -> int:
    '''
    This method queries the user for an integer
    between the lower bound and upper bound inclusive.
    '''
    while True:
        try:
            s = int(input(msg))
            if s >= lower_bound and s <= upper_bound:
                return s
        except:
            pass


def print_cli_help() -> None:
    '''
    This function prints the help for
    the cli.
    '''
    print('''a,attack -> run an attack
q,quit   -> quit the cli
h,help   -> print this help message
    ''')


def run_cli_loop() -> None:
    '''
    This function runs the CLI input loop.
    '''
    print_cli_help()
    while True:
        colors.header()
        command = input('Enter Command: ')
        colors.endc()
        if command == 'a' or command == 'attack':
            colors.okblue()
            attacking_armies = get_int_in_bounds('Input Attacking Armies: ', 2, 1000)
            defending_armies = get_int_in_bounds('Input Defending Armies: ', 1, 1000)
            uppr = min(3, attacking_armies-1)
            attacking_dice = 0
            if uppr > 1:
                attacking_dice = get_int_in_bounds('Input Attacking Dice [1, %d]: ' % uppr, 1, uppr)
            else:
                attacking_dice = 1
                print('Input Attacking Dice [1, %d]: 1' % uppr)
            uppr = min(2, defending_armies)
            if uppr > 1:
                defending_dice = get_int_in_bounds('Input Defending Dice [1, %d]: ' % uppr, 1, uppr)
            else:
                defending_dice = 1
                print('Input Defending Dice [1, %d]: 1' % uppr)
            colors.endc()
            while attacking_armies > 1 and defending_armies > 0:
                if attacking_armies == 3 and attacking_dice > 2:
                    attacking_dice = 2
                elif attacking_armies == 2 and attacking_dice > 1:
                    attacking_dice = 1
                if defending_armies == 1 and defending_dice > 1:
                    defending_dice = 1
                colors.warning()
                print('Attacking With %d Dice' % attacking_dice)
                print('Defending With %d Dice' % defending_dice)
                result = get_casualties(attacking_dice, defending_dice)
                attacking_armies -= result[0]
                defending_armies -= result[1]
                print('Attacker Lost: %d' % result[0])
                print('Defender Lost: %d' % result[1])
                print('Attacker Armies Remaining: %d' % attacking_armies)
                print('Defender Armies Remaining: %d' % defending_armies)
                colors.endc()
                if attacking_armies > 1 and defending_armies > 0:
                    colors.header()
                    cont = input('Continue Attacking? (Y/n): ')
                    colors.endc()
                    if cont == 'no' or cont == 'n':
                        break
            colors.okgreen()
            if defending_armies == 0:
                print('Attackers Won!')
            elif attacking_armies == 1:
                print('Attackers Repulsed!')
                savout1 = os.dup(1)
                savout2 = os.dup(2)
                os.close(1)
                os.close(2)
                try:
                    webbrowser.open('https://www.youtube.'
                                    'com/watch?v=dQw4w9WgXcQ')
                finally:
                    os.dup2(savout1, 1)
                    os.dup2(savout2, 2)
            colors.endc()
        elif command == 'q' or command == 'quit':
            break
        elif command == 'h' or command == 'help':
            print_cli_help()
        else:
            print('Unknown Command: %s' % command)
            print_cli_help()


if __name__ == '__main__':
    run_cli_loop()
