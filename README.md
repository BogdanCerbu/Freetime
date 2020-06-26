# Freetime
Practices

1)

Story

You plan to play Risk with some friends but you suddenly realize you lost all your dice. As your evening is well planned, you can't let your friends down, so you start to write a script that helps you out.

Description

Write a python script, that generates 5 numbers between 1 and 6 and prints them in a meaningful way for the game. Sort the results for the attacker and for the defender, so make roll pairs, like in this image:



Decide how many armies you are going to use in your attack. Because your territory must be occupied at all times, you must leave at least one army behind. The number of armies you attack with will determine how many dice you get to roll when you square off the opponent whose territory you are defending.[12]
1 army = 1 die
2 armies = 2 dice
3 armies = 3 dice

Roll the dice. You roll up to three red dice, depending on your troop size. The defending player rolls the same number of white dice as the number of troops in their defending territory, with a maximum of two.[13]
Match up the highest red die with the highest white die, and match the second highest red die with the second highest white die. If there is only one white die, only match up the highest red die with the white die.[14]
Remove one of your pieces from the attacking territory if the white die is higher or equal to its corresponding red die.
Remove one of your opponent’s pieces from the defending territory if the red die is higher to its corresponding white die.


def roll_dice(p1_army,p2_army):
    if p1


In a dice pair, there are the following rules:

When the attacker's die value is larger: Attacker wins (1 defender unit dies)
When the 2 dice value is tie: Defender wins (1 attacker unit dies)
When the defender's die value is larger: Defender wins (1 attacker unit dies)