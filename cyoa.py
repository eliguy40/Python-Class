import time

print("Welcome to choose your own adventure!")

nombre = input("What's your name? ")
print("Hey,", nombre,"!")
print("You're in a bustling city. Where would you like to go? There's a grocery store, a pizza place, or if you want to, you can talk to a man next to you!")
time.sleep(3)
choice = input("(G)rocery Store, (P)izza Place, (T)alk to man next to you\n").upper()
if choice == "G":
    print("You go into the grocery store. What food would you like to get?")
    food = input("(T)urkey, (A)vacado, (C)hex Mix\n").upper()
    if food == "T":
        print("You bought a live turkey. After leaving the grocery store, it immedietly runs away. Goodbye! =)")
    if food == "A":
        print("After coming home and eating the avacado, you suddenly have an intense craving for more avacados. Over the coming months and years, you will proceed to eat every avacado in the entire world, making them extinct. Cool!")
    if food == "C":
        print("You go home and enjoy some delicious chex mix before being suddenly abducted by aliens. Cya!")
elif choice == "P":
    print("You decided to go to the Pizza Place. The smell of freshly baked dough invades your nostrils. What kind of pizza should you get?")
    pizza = input("(P)epperoni, (C)heese, or (H)awaiian\n").upper()
    if pizza == "P":
        print("Good choice! Pepperoni is the superior type of pizza. You live happily ever after.")
    if pizza == "C":
        print("How DARE you. How absolutely DARE you. Just get pepperoni! It's infinitely better and even if you don't like the pepperoni itself that much, you can just take them off and eat your pizza that way! I have no clue why you chose this. Please seek help.")
    if pizza == "H":
        print("...I'm not going to say anything about this choice because I don't want to argue with everyone for 3 hours. That was a choice that you just made.")
elif choice == "T":
    print("You decide to have a conversation with the man standing next to you. What would you like to talk about?")
    topic = input("Talk about the (G)rocery store over next to you, the (P)izza place, or as a (Q)uestion about him.\n").upper()
    if topic == "G":
        print("He says, 'I love going there and usually get chex mix because unfortunately they don't kill their turkies before selling them and the avocados are a bit too addictive...' He then leaves and in the distance you can see a UFO following him closely...")
    if topic == "P":
        print("The man immediatly becomes uncomfortable and asks, 'What about it?' You ask him which pizza he would get and he replies, 'I love hawaiian'. You immediatly run away as fast as you can. Hopefully you never see him again!")
    if topic == "Q":
        print("You ask him why he's here in this bustling city and he replies saying, 'nothing much! Just doing some street photography because it's a pretty cool hobby that someone who is making this might enjoy doing every so often. Therefore I'm very cool.'")
else:
    print("That's not a correct letter! Try again")
    quit()
print("I hope you enjoyed this little game I made! Try again to see all of the different outcomes you can do! =D")