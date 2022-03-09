import random

while True:
    print(random.randint(1,6))

    another_roll = input("Want you roll this dice again? y/n: ")
    if another_roll.lower() == "y":
       continue
    
    else:
        break