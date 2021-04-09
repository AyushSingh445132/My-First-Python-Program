# Buit in Modules
import random

flag = True
while flag:
    num = input("Type for to which you want the guess upto:- ")

    if num.isdigit():
        print("Let's start the Game!")
        num = int(num)
        flag = False
    else:
        print("Invalid Input!Try again!")

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    guess = input("Type a number between 1 and "+ str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)

    if guess==secret:
        print("You have guessed the number")
    else :
        print("Wrong Number! Try again")
        count += 1

print("It took you",count,"trys to guess the correct number.")

# External Modules