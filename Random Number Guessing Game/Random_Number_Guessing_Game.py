from itertools import count
import random

flag = True
while flag:
    num = input("Type a number for an upper bound: ")

    if num.isdigit():
        print("let's Play")
        num = int(num)
        flag = False
    else:
        print("Invalid input! Try Again")

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = input('Please a number between 1 and ' + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print("You got it")
    else:
        print("Please Try Again")
        count += 1

print("It took you" + num + "guess")