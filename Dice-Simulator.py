import DiceLogos as logo
import random

print('''
    DICE SIMULATOR!
''')
flag = True
while flag:
    choice = input("Roll the dice? (y/n): ")
    if choice == 'y':

        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)

        print(f"Dice rolled {number1} and {number2}\n")
        print(logo.l[number1])
        print(logo.l[number2])
        flag = True
    else:
        flag = False
