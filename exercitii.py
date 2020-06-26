import random


def roll_dice(attacking_army, defending_army):
    red_dice = 0
    white_dice = 0
    if attacking_army == 1:
        red_dice = 1                            # for x in range(3):
    elif attacking_army == 2:                    # if attacking_army == x:
        red_dice = 2                            # red_dice = x
    elif attacking_army > 2:                    #
        red_dice = 3
    if defending_army == 1:
        white_dice = 1
    elif defending_army > 1:  # maximum of 2 dices for defender
        white_dice = 2
    roll_red = [random.randrange(1, 6) for x in range(0, red_dice)]
    roll_white = [random.randrange(1, 6) for x in range(0, white_dice)]
    roll_red = sorted(roll_red)
    roll_white = sorted(roll_white)
    print('\nAttacking player rolled: ', roll_red)
    print('\nDefending player rolled: ', roll_white)
    if white_dice == 1:
        if roll_white[0] >= roll_red[len(roll_red)-1]:
            print('Defender wins! Attacker loses 1 army')
            attacking_army -= 1
        else:
            print('Attacker wins! Defender loses 1 army')
            defending_army -= 1
    for i in range(1, len(roll_white)):
        if roll_white[i] >= roll_red[i]:
            print('Defender wins! Attacker loses 1 army')
            attacking_army -= 1
        else:
            print('Attacker wins! Defender loses 1 army')
            defending_army -= 1
    return (attacking_army, defending_army)


print(roll_dice(3, 1))
