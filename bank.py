import random
import time

x = 0
points = 0
dice = int(1)
dice2 = int(1)
keepplaying = "y"

input("Time to play Bank! You can roll as many times as you want, with rolling doubles doubles your points, but if you roll a 7 then you lose! (hit enter)")
input("In the first three rounds you actually can't lose and getting a 7 instead gives you 70 points! Doubling doesn't count though. Ready to start? (hit enter)")

start = input("Start? (y/n)\n")

if start == "y":
    while x < 3:
        print("You currently have", points, "points.")
        time.sleep(1)
        keepplaying = input("Press enter for next roll:")
        dice = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print ("/---\    /---\ ")
        print ("|", dice, "|    |", dice2, "| ")
        print ("\---/    \---/ ")
        if dice + dice2 != 7:
            points = points + dice + dice2
        if dice + dice2 == 7:
            print("You rolled a 7! You now have 70 more points.")
            points = points + 70
        x = x + 1
        # first three rounds end
    print("Points:", points)
    time.sleep(2)
    print("Alright, now 7s are bad and doubles count!")
    dice = 0
    dice2 = 0
    while dice + dice2 > int(7) or dice + dice2 < 7:
        if dice != dice2 and dice + dice2 != 0:
            points = points + int(dice) + int(dice2)
            print("Phew! You didn't roll a 7! Points:", points)
        if dice == dice2 and dice + dice2 != 0:
            print("Doubles! Your points are twice as much now!")
            points = points * 2
            print("Points:", points)
        time.sleep(1)
        keepplaying = input("Keep playing? (y/n)\n")
        if keepplaying == "n":
            print("Banking so soon? You earned a total of..."), time.sleep(2), print(points, "points!")
            quit()
        # dice rolling mechanic
        dice = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print ("/---\    /---\ ")
        print ("|", dice, "|    |", dice2, "| ")
        print ("\---/    \---/ ")

    points = 0
    print("Uh oh! You rolled a 7! You lost ALL of your points!! Try again!")
    quit()
elif start == "n":
    print("You're lame.")
    quit()
else:
    print("That's not a correct input. Try again!")
    quit()
