'''
This module finds the probabilities associated
with certain setups in a game of Risk.
'''

from typing import Callable
from risk_rolled import get_casualties


def get_probability_win(num_attacking: int,
                        num_defending: int,
                        dice_attacking_func: Callable[[int, int], int],
                        dice_defending_func: Callable[[int, int], int],
                        sample_size: int) -> float:
    '''
    This function gets the approximate
    probability of winning if you are attacking
    with num_attacking dice against an enemy who
    has num_defending dice, using dice_attacking_func
    to return the number of dice that you will attack with
    at each stage, and dice_defending_func to do the same
    for the defender.  It will run this test sample_size
    number of times and return the found probability.
    '''
    num_wins = 0
    casualties = (0, 0)
    num_attacking_saved = num_attacking
    num_defending_saved = num_defending
    for i in range(sample_size):
        while num_attacking > 1 and num_defending > 0:
            attacking_dice = dice_attacking_func(num_attacking, num_defending)
            defending_dice = dice_defending_func(num_attacking, num_defending)
            casualties = get_casualties(attacking_dice, defending_dice)
            num_attacking -= casualties[0]
            num_defending -= casualties[1]
        if num_defending == 0:
            num_wins += 1
        num_attacking = num_attacking_saved
        num_defending = num_defending_saved
    return num_wins / sample_size

def get_attacker_dice(num_attacking: int, num_defending: int) -> int:
    if num_attacking > 3:
        return 3
    elif num_attacking == 3:
        return 2
    elif num_attacking == 2:
        return 1
    else:
        raise RuntimeError('We shouldn\'t be here!')

def get_defender_dice(num_attacking: int, num_defending: int) -> int:
    if num_defending >= 2:
        return 2
    elif num_defending == 1:
        return 1
    else:
        raise RuntimeError('We shouldn\'t be here!')

if __name__ == '__main__':
    while True:
        num_attacking = int(input('Number Attacking: '))
        num_defending = int(input('Number Defending: '))
        sample_size = int(input('Sample Size: '))
        print(get_probability_win(num_attacking, num_defending,
              get_attacker_dice, get_defender_dice, sample_size))
