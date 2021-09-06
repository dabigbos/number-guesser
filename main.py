
import random


guesses = 0
print("What's your name?")
name=input()
correctnum = random.randint(1,10000)
correctlim = random.randint(1,100)
print(name + ", you will be guessing my number today. I will think of a random number in my head. You will need to guess the number.")
print("Which mode would you like to enter? Infinite or Limited 20 tries? Enter 1 for infinite and enter 2 for limited")
gamemode=input()
guesses=0

if int(gamemode)==1:
    print("guess a number between 1 and 10000")
    print("enter your number below")
    while True:

        numberguessed = input()
        if int(numberguessed)>correctnum:
            print("Try again, number too high.")
            guesses=guesses+1

        if int(numberguessed)<correctnum:
            print("try again, number too low.")
            guesses=guesses+1

        if int(numberguessed)==correctnum:
            guesses = guesses + 1
            break

    print("The number was " + str(correctnum)+"! You used " + guesses + " guesses!")

if int(gamemode)==2:
    print("You have chosen limited gamemode! This is a Hard gamemode.")
    print("Here are the rules:")
    print("You have 10 tries to guess the number I'm thinking off between 1 and 100")
    print("enter your number below")
    while guesses<=10:
        numberguessed = input()
        if int(numberguessed) > correctlim:
            print("Try again, number too high.")
            guesses = guesses + 1

        if int(numberguessed) < correctlim:
            print("try again, number too low.")
            guesses = guesses + 1

        if int(numberguessed) == correctlim:
            guesses = guesses + 1
            print("Great job," + name + ", you won limited mode!")
            break


