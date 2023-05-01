import random


def integer_guess(prompt):
    while True:
        temp=input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:
        print("plz enter the valid number")


help(integer_guess)
highest = 1000
answer =random.randint(1, highest)
print(answer)
guess=0
print("guess the number between 1 and 1000")
while guess!=answer:
    guess=integer_guess(": ")

    if guess==0:
        break
    if guess==answer:
        print("you guessed it correctly")
    if guess<answer:
        print("please guess higher")
    if guess>answer:
        print("please guess lower")
