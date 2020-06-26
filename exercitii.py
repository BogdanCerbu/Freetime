import random


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
    elif defending_army > 1:  # maximum of 2 dices for defender
        white_dice = 2
    roll_red = sorted([random.randrange(1, 6) for x in range(0, red_dice)])
    roll_white = sorted([random.randrange(1, 6) for x in range(0, white_dice)])
    print('\nAttacking player rolled: ' + "".join(roll_dice))
    print('\nDefending player rolled: ' + "".join(roll_white))
    if white_dice == 1:  # If there is only one white die, only match up the highest red die with the white die
        if roll_white[0] >= roll_red[0]:
            print('Defender wins! Attacker loses 1 army')
            attacking_army -= 1
        else: 
            print('Attacker wins! Defender loses 1 army')
            defending_army -= 1


# print(sorted(roll_red))