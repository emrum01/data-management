import random

dice1 = random.randrange(6) + 1
dice2 = random.randrange(6) + 1
total = dice1 + dice2

print("What is your name?")

yourName = input()
print("Hello, {}!".format(yourName))
print("Rolling the dice...")
print("Dice 1: {}\nDice 2: {}".format(dice1, dice2))
print("Total value: {}".format(total))

if total > 7:
    print("{} won!".format(yourName))
else:
    print("{} lost!".format(yourName))
