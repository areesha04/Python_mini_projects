import random
inp="Y"
while inp == "Y":
    x = random.randrange(1,6)

    if x == 1:
        print("--------------")
        print("|            |")
        print("|     0      |")
        print("|            |")
        print("--------------")
    if x == 2:
        print("--------------")
        print("|0           |")
        print("|            |")
        print("|           0|")
        print("--------------")
    if x == 3:
        print("--------------")
        print("|0           |")
        print("|     0      |")
        print("|           0|")
        print("--------------")
    if x == 4:
        print("--------------")
        print("| 0        0 |")
        print("|            |")
        print("| 0        0 |")
        print("--------------")
    if x ==5:
        print("--------------")
        print("| 0        0 |")
        print("|     0      |")
        print("| 0        0 |")
        print("--------------")

    inp = input("Do you want to roll the dice again? Y/N")


