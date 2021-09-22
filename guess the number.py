import random
number= random.randrange(1,50)
guess = int (input ("Guess a number in between 1 and 50"))
wrong=0
while number != guess:

    wrong=wrong+1
    if wrong == 2:
        print("you loose")
        break

    if guess < number :

        print("you need to think of a greater number, try again!")
        guess = int (input ("Guess a number in between 1 and 50"))

    elif guess > number:

        print ("you need to think of a smaller number, try again!")
        guess = int(input("Guess a number in between 1 and 50"))


print("you guessed a correct number")