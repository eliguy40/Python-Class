import random
import time
thing = "meep"
critChecker = "food"
yourHp = "yes"
selfDamage = 0
yourPokemon = "cheese"
notYourHp = "yes"
notYourPokemon = "stillCheese"
squirtleAttacks = ["tackle", "water gun", "skull bash"]
bulbasaurAttacks = ["tackle", "razor leaf", "vine whip", "skull bash"]
charmanderAttacks = ["tackle", "skull bash", "ember"]
yourAttack = "alsoCheese"
notYourAttack = "yetAgainCheese"
attackChecker = 0
pokeball = 5
caught = 0
attackTurn = random.randint(0, 1)
def battle():
# This to line 48 is the setup of the game.
    global yourHp, yourPokemon, notYourHp, notYourPokemon, yourAttack, notYourAttack, attackChecker, selfDamage, attackTurn, critChecker, pokeball, caught, thing
    print("Welcome to the Pokemon battle simulator")
    yourPokemon = input("Please choose a pokemon, your choices are... bulbasaur, charmander, and squirtle. Or if you need help, type 'help' to learn how to play the game: ").lower()
    if yourPokemon == "bulbasaur":
        print("You chose bulbasaur.")
    elif yourPokemon == "charmander":
        print("You chose charmander.")
    elif yourPokemon == "squirtle":
        print("You chose squirtle")
    elif yourPokemon == "help":
        print("There are 2 actions you can do with your turn, those actions are: ")
        print("---------------------------------------")
        print("Attack: you can type in an attack from the attack list when you select a pokemon, if you didn't type in an attack right you will see the action prompt pop up again.")
        print("---------------------------------------")
        print("Catch: you can attempt to catch the pokemon with the 'catch' command, the attempted capture has a chance to sucseed or fail depending on the remaining health of the target pokemon, your best bet is to wait untill you get the 'badly hurt' text then type in 'catch'")
        print("---------------------------------------")
        print("please reboot the program.")
        print()
    else:
        print("There appeared to be an error in how you spelled your pokemon.")
    yourHp = random.randint(200, 250)
    notYourPokemon = random.randint(1, 3)
    notYourHp = random.randint(200, 250)
    if notYourPokemon == 1:
        notYourPokemon = "bulbasaur"
    elif notYourPokemon == 2:
        notYourPokemon = "charmander"
    else:
        notYourPokemon = "squirtle"
    print(yourPokemon, " vs. ", notYourPokemon)
    if yourPokemon == "charmander":
        print("Your Pokemon's moves are:", charmanderAttacks)
    elif yourPokemon == "bulbasaur":
        print("Your Pokemon's moves are:", bulbasaurAttacks)
    elif yourPokemon == "squirtle":
        print("Your Pokemon's moves are:", squirtleAttacks)
    else:
        print("Uhhhhh... you lose, I guess?")
        yourHp = -1
        
# This to line 237 is your attacks.

    while yourHp >= 0 and notYourHp >= 0 and caught <= 1:
        if attackTurn == 1 and caught == 0:
            yourAttack = input("Type in your attack: ")
            if yourAttack == "catch" and pokeball >= 0:
                print("You threw the pokeball.")
                time.sleep(1)
                for x in range(random.randint(0, 3)):
                    print("...")
                    time.sleep(1)
                attackChecker = random.randint(1, 0.2 * notYourHp)
                if attackChecker <= 6:
                    caught = 1
                    print("You caught a ", notYourPokemon, "!")
                else:
                    print("The ", notYourPokemon, " escaped...")
                    attackTurn = 0
                    pokeball = pokeball - 1
                    print("You have ", pokeball, " Pokeballs left.")
            critChecker = random.randint(1, 15)
            if yourAttack == "tackle":
                time.sleep(random.randint(0, 2))
                attackChecker = random.randint(1, 10)
                if attackChecker == 1:
                    print("Your attack misses")
                    attackTurn = 0
                else:
                    time.sleep(random.randint(0, 2))
                    notYourHp = notYourHp - random.randint(20, 40)
                    attackTurn = 0
                    if notYourHp <= 30 and notYourHp >= 0:
                        print("The opposing ", notYourPokemon, " seems hurt.")
                    
            if yourPokemon == "squirtle":
                if yourAttack == "water gun":
                    time.sleep(random.randint(0, 2))
                    attackChecker = random.randint(1, 10)
                    if attackChecker == 1:
                        print("Your attack misses")
                        attackTurn = 0
                        
                    else:
                        if notYourPokemon == "bulbasaur" and attackChecker >= 1:
                            notYourHp = notYourHp - random.randint(30, 50) * 0.5
                            notYourHp = round(notYourHp)
                            time.sleep(random.randint(0, 2))
                            if attackChecker >= 1:
                                print("It's not very effective...")
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                                
                        elif notYourPokemon == "charmander" and attackChecker >= 1:
                            notYourHp = notYourHp - random.randint(30, 50) * 2
                            time.sleep(random.randint(0, 2))
                            if attackChecker <= 1:
                                print("It's super effective!")
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
                        else:
                            notYourHp = notYourHp - random.randint(30, 50)
                            time.sleep(random.randint(0, 2))
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
                elif yourAttack == "skull bash":
                    attackChecker = random.randint(1, 10)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print("Your attack misses")
                        attackTurn = 0
                    else:
                        selfDamage = random.randint(1, 3)
                        if selfDamage == 1:
                            time.sleep(random.randint(0, 2))
                            selfDamage = random.randint(15, 30)
                            yourHp = yourHp - selfDamage
                            print("Squirtle took: ", selfDamage, " Damage")
                            notYourHp = notYourHp - random.randint(35, 55)
                            print("Your hp is: ", yourHp)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
                        else:
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(35, 55)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
            elif yourPokemon == "charmander":
                if yourAttack == "ember":
                    attackChecker = random.randint(1, 9)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print("Your attack misses")
                        attackTurn = 0
                        
                    if notYourPokemon == "squirtle" and attackChecker >= 1:
                        time.sleep(random.randint(0, 2))
                        notYourHp = notYourHp - random.randint(15, 50) * 0.5
                        notYourHp = round(notYourHp)
                        if attackChecker >= 1:
                            print("It's not very effective...")
                        attackTurn = 0
                        if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                        
                    elif notYourPokemon == "bulbasaur" and attackChecker >= 1:
                        time.sleep(random.randint(0, 2))
                        notYourHp = notYourHp - random.randint(15, 50) * 2
                        if attackChecker >= 1:
                            print("It's super effective!")
                        attackTurn = 0
                        if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                        
                    else:
                        time.sleep(random.randint(0, 2))
                        notYourHp = notYourHp - random.randint(15, 50)
                        attackTurn = 0
                        if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                        
                elif yourAttack == "skull bash":
                    attackChecker = random.randint(1, 10)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print("Your attack misses")
                        attackTurn = 0
                        
                    else:
                        time.sleep(random.randint(0, 2))
                        selfDamage = random.randint(1, 3)
                        if selfDamage == 1:
                            selfDamage = random.randint(15, 30)
                            yourHp = yourHp - selfDamage
                            print("Charmander took: ", selfDamage, " Damage")
                            notYourHp = notYourHp - random.randint(35, 55)
                            print("Your hp is: ", yourHp)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
                        else:
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(35, 55)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
            elif yourPokemon == "bulbasaur":
                if yourAttack == "razor leaf":
                    attackChecker = random.randint(1, 7)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print("Your attack misses")
                        attackTurn = 0
                        
                    else:
                        if notYourPokemon == "charmander":
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(30, 60) * 0.5
                            notYourHp = round(notYourHp)
                            if attackChecker >= 1:
                                print("It's not very effective...")
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                                
                        elif notYourPokemon == "squirtle":
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(30, 60) * 2
                            if attackChecker >= 1:
                                print("It's super effective!")
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                                
                        else:
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(30, 60)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
                elif yourAttack == "vine whip":
                    time.sleep(random.randint(0, 2))
                    attackChecker = random.randint(1, 13)
                    if attackChecker == 1:
                        print("Your attack misses")
                        attackTurn = 0
                    else:
                        if notYourPokemon == "charmander":
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(20, 40) * 0.5
                            notYourHp = round(notYourHp)
                            if attackChecker >= 1:
                                print("It's not very effective...")
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                                
                        elif notYourPokemon == "squirtle":
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(20, 40) * 2
                            if attackChecker >= 1:
                                print("It's super effective!")
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")

                        else:
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(20, 40)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                    
                elif yourAttack == "skull bash":
                    attackChecker = random.randint(1, 10)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print("Your attack misses")
                        attackTurn = 0
                        
                    else:
                        time.sleep(random.randint(0, 2))
                        selfDamage = random.randint(1, 3)
                        if selfDamage == 1:
                            selfDamage = random.randint(15, 30)
                            yourHp = yourHp - selfDamage
                            print("bulbasaur took: ", selfDamage, " Damage")
                            notYourHp = notYourHp - random.randint(35, 55)
                            print("Your hp is: ", yourHp)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
                        else:
                            time.sleep(random.randint(0, 2))
                            notYourHp = notYourHp - random.randint(35, 55)
                            attackTurn = 0
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
            else:
                print("cheese")
                attackTurn = 0
                
            if critChecker == 1 and attackChecker >= 1:
                print("A critical hit!")
                notYourHp = notYourHp - 30
                
# This is the opponent's code.
        
        elif caught == 0:
            critChecker = random.randint(1, 15)
            if notYourPokemon == "squirtle":
                notYourAttack = "skull bash"
                if notYourAttack == "tackle":
                    print("The opposing squirtle used tackle")
                    attackChecker = random.randint(1, 10)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack.")
                        attackTurn = 1
                        
                    else:
                        time.sleep(random.randint(0, 2))
                        yourHp = yourHp - random.randint(20, 40)
                        print(yourHp)
                        attackTurn = 1
                        
                elif notYourAttack == "skull bash":
                    time.sleep(random.randint(0, 2))
                    print("The opposing squirtle used skull bash.")
                    attackChecker = random.randint(1, 9)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, "avoided the attack.")
                        attackTurn = 1
                    else:
                        selfDamage = random.randint(1, 3)
                        if selfDamage == 1:
                            time.sleep(random.randint(0, 2))
                            selfDamage = random.randint(15, 30)
                            notYourHp = notYourHp - selfDamage
                            print("The opposing squirtle took: ", selfDamage, " Damage")
                            yourHp = yourHp - random.randint(35, 55)
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                                
                        else:
                            yourHp = yourHp - random.randint(35, 55)
                            time.sleep(random.randint(0, 2))
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")
                            
                elif notYourAttack == "water gun":
                    time.sleep(random.randint(0, 2))
                    print("The opposing squirtle used water gun.")
                    attackChecker = random.randint(1, 9)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack")
                        attackTurn = 1
                    else:
                        if yourPokemon == "charmander":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(30, 50) * 2
                            print("It's super effective!")
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                        elif yourPokemon == "bulbasaur":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(30, 50) * 0.5
                            yourHp = round(yourHp)
                            print("It's not very effective...")
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                        else:
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(30, 50)
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                else:
                    print("cheese")
                    
            elif notYourPokemon == "charmander":
                notYourAttack = random.choice(charmanderAttacks)
                if notYourAttack == "ember":
                    time.sleep(random.randint(0, 2))
                    print("The opposing charmander used ember.")
                    attackChecker = random.randint(1, 9)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack")
                        attackTurn = 1
                    else:
                        if yourPokemon == "squirtle":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(15, 50) * 0.5
                            yourHp = round(yourHp)
                            print("It's not very effective...")
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                        elif yourPokemon == "bulbasaur":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(15, 50) * 2
                            print("It's super effective!")
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                        else:
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(15, 50)
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                            
                elif notYourAttack == "skull bash":
                    time.sleep(random.randint(0, 2))
                    print("The opposing charmander used skull bash")
                    attackChecker = random.randint(1, 9)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack.")
                        attackTurn = 1
                    else:
                        time.sleep(random.randint(0, 2))
                        attackChecker = random.randint(1, 10)
                        if attackChecker == 1:
                            print(yourPokemon, " avoided the attack.")
                            attackTurn = 1
                        else:
                            selfDamage = random.randint(1, 3)
                            if selfDamage == 1:
                                selfDamage = random.randint(10, 30)
                                notYourHp = notYourHp - selfDamage
                                yourHp = yourHp - random.randint(35, 55)
                                print("the opposing charmander took ", selfDamage, " damage")
                                print("your hp is: ", yourHp)
                                attackTurn = 1
                                if notYourHp <= 30 and notYourHp >= 0:
                                    print("The opposing ", notYourPokemon, " seems hurt.")
                                
                            else:
                                yourHp = yourHp - random.randint(35, 55)
                                print("Your hp is:", yourHp)
                                attackTurn = 1
                                
                elif notYourAttack == "tackle":
                    time.sleep(random.randint(0, 2))
                    print("The opposing charmander used tackle.")
                    attackChecker = random.randint(1, 10)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack.")
                        attackTurn = 1
                        
                    else:
                        time.sleep(random.randint(0, 2))
                        yourHp = yourHp - random.randint(20, 40)
                        print("your hp is:", yourHp)
                        attackTurn = 1
                        
            elif notYourPokemon == "bulbasaur":
                notYourAttack = random.choice(bulbasaurAttacks)
                if notYourAttack == "tackle":
                    time.sleep(random.randint(0, 2))
                    print("The opposing bulbasaur used tackle.")
                    attackChecker = random.randint(1, 10)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack.")
                        attackTurn = 1
                    else:
                        time.sleep(random.randint(0, 2))
                        yourHp = yourHp - random.randint(20, 40)
                        print("your hp is:", yourHp)
                        attackTurn = 1
                        
                elif notYourAttack == "skull bash":
                    time.sleep(random.randint(0, 2))
                    print("The opposing bulbasaur used skull bash")
                    attackChecker = random.randint(1, 9)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack.")
                        attackTurn = 1
                    else:
                        selfDamage = random.randint(1, 3)
                        if selfDamage == 1:
                            selfDamage = random.randint(10, 30)
                            notYourHp = notYourHp - selfDamage
                            yourHp = yourHp - random.randint(35, 55)
                            print("the opposing bulbasaur took ", selfDamage, " damage")
                            print("your hp is: ", yourHp)
                            attackTurn = 1
                            if notYourHp <= 30 and notYourHp >= 0:
                                print("The opposing ", notYourPokemon, " seems hurt.")

                        else:
                            yourHp = yourHp - random.randint(35, 55)
                            print("Your hp is:", yourHp)
                            attackTurn = 1
                            
                elif notYourAttack == "razor leaf":
                    time.sleep(random.randint(0, 2))
                    print("The opposing bulbasaur used razor leaf.")
                    attackChecker = random.randint(1, 7)
                    if attackChecker == 1:
                        time.sleep(random.randint(0, 2))
                        print(yourPokemon, " avoided the attack.")
                        attackTurn = 1
                        
                    else:
                        if yourPokemon == "charmander":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(30, 60) * 0.5
                            yourHp = round(yourHp)
                            print("It's not very effective...")
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                        elif yourPokemon == "squirtle":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(30, 60) * 2
                            print("It's super effective!")
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                        else:
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(30, 60)
                            print("Your hp is: ", yourHp)
                            attackTurn = 1
                            
                elif notYourAttack == "vine whip":
                    time.sleep(random.randint(0, 2))
                    print("The opposing bulbasaur used vine whip")
                    attackChecker = random.randint(1, 13)
                    if attackChecker == 1:
                        print(yourPokemon, " avoided the attack")
                        attackTurn = 1
                        
                    else:
                        if yourPokemon == "charmander":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(20, 40) * 0.5
                            yourHp = round(yourHp)
                            print("It's not very effective...")
                            print("your hp is: ", yourHp)
                            attackTurn = 1
                            
                        elif yourPokemon == "squirtle":
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(20, 40) * 2
                            print("It's super effective!")
                            print("your hp is: ", yourHp)
                            attackTurn = 1
                            
                        else:
                            time.sleep(random.randint(0, 2))
                            yourHp = yourHp - random.randint(20, 40)
                            print("your hp is: ", yourHp)
                            attackTurn = 1
                            
            if critChecker == 1 and attackChecker >= 1:
                print("A critical hit!")
                yourHp = yourHp - 30

    if yourHp <= 1 and notYourHp >= 0:
        print()
        print("Your ", yourPokemon, " fainted.")
        print("You lost...")
        print()
        
    elif yourHp >= 0 and notYourHp <= 1 and caught == 0:
        print()
        print("The opposing ", notYourPokemon, " fainted.")
        print("You won!")
        print()
        
    else:
        print()
        print("Both pokemon fainted...")
        print()

battle()