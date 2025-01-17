import random
import time

print(" ~ LET'S GO GAMBLING (we're about to lose it all :D) ~ \n")
print("rules: you have a 2/3rds chance to win, but 1/3rd to lose. If you lose, you lose")
print("EVERYTHING! Try to get as far as you can!\n")
input("-type something in to continue-")

points = 0
print("Points: ", points)
print("(S)tart/(Q)quit")
player = input()
rand = 1
x = 0
if str(player) == "S":
    while rand == 1 or 2:
        print("(K)eep going/(Q)quit")
        player == input()
        if str(player) == "K":
            rand = random.randint(1, 3)
            if rand == 1:
                print("Today's lesson, KEEP GAMBLING")
                points += 5
                print("+", points, " Points! (Lucky!)")
            if rand == 2:
                print("Today's lesson, KEEP GAMBLING")
                points += 2
                print("+", points, "Points!")
            if rand == 3:
                print("LOOOL YOU LOST IT ALL")
                exit()
        if str(player) == "Q":
            print("Cya chump. I guess you'll go away with...", points, "points!")
            exit()
if str(player) == "Q":
   print("Cya chump. I guess you'll go away with...", points, "points!")
   exit()
else:
    print("That's invalid")