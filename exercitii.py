from math import random


def roll_dice(attacking_army, defending_army):
    red_dice = 0
    white_dice = 0
    if attacking_army == 1:
        red_dice = 1
    elif attacking_army == 2:
        red_dice = 2
    elif attacking_army > 2:
        red_dice = 3
    if defending_army == 1:
        white_dice = 1
    elif defending_army > 1:  #maximum of 2 dices for defender
        white_dice = 2
