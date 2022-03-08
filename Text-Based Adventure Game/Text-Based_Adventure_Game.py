# Nested if else
i = 0
while i <= 2:
    answer = input("Who you like to play? (yes/no) ")

    if answer.lower().strip() == "yes":
        answer = input(
            "You reach a crossroads, would you like to left or right? ").lower().strip()
        if answer == "left":
            answer = input(
                "You encounter a monster, would you like to run or attack? ")

            if answer == "attack":
                print(
                    f"That was not  greatest idea, you lost! try again You have more {2-i} chance to play")
            elif answer == "run":
                print("Good Choic, you made it away safely.")
                answer = input(
                    "You see a car and plane, which would you like to take? (car/plane) ")
                if answer == "plane":
                    print(f"Unfortunently you don't know how to fly.....Game Over! ")
                else:
                    print("You Won! ")
            else:
                print(
                    f"Invalied Input! You have to write (run or attack) properly try again you have more {2-i} chance to play")

        elif answer == "right":
            print(
                f"You walk aimlessly to the right and fall on a patch of ice. You ingure your leg and can't continue. Game over! try again you have more {2-i} chance to play ")
        else:
            print(
                f"Invalied Input! You have to write (left or right) properly try again you have more {2-i} chance to play")

    else:
        print(
            f"That's so bad!, you have total 3 chance so be carefull let's Try Again You have left: {2-i} ")

        if i == 2:
            print("You are so bad to play")

    i += 1


# About This Game Developer

# git = https://github.com/Rasel1435

# Linkden = https://www.linkedin.com/in/shekhnirob1