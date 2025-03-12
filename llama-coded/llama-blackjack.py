# Made with llama3.1:8b!
# **How to Play**
# 
# 1. Run the game by executing the Python script.
# 2. You will be dealt two cards and shown the dealer's up card.
# 3. Choose whether you want to 'hit' (take another card) or 'stand' (keep your current hand).
# 4. If you go over 21, you bust! The dealer wins.
# 5. After you stand, the dealer draws cards until they have a hand value of 17 or higher.
# 6. Compare your final hand values with the dealer's to determine the winner.
# 
# Note: This is a simplified version of Blackjack and does not include features like insurance, double down, or 
# splitting pairs.

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            if card.value.isnumeric():
                value += int(card.value)
            else:
                if card.value == 'A':
                    aces += 1
                    value += 11
                elif card.value in ['K', 'Q', 'J']:
                    value += 10

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        player_hand = Hand()
        dealer_hand = Hand()

        for _ in range(2):
            player_hand.add_card(self.deck.deal_card())
            dealer_hand.add_card(self.deck.deal_card())

        print(f"Player's hand: {player_hand.cards}, Value: {player_hand.get_value()}")
        print(f"Dealer's up card: {dealer_hand.cards[0]}")

        while True:
            action = input("Do you want to 'hit' or 'stand'? ")

            if action.lower() == 'hit':
                player_hand.add_card(self.deck.deal_card())
                print(f"Player's hand: {player_hand.cards}, Value: {player_hand.get_value()}")

                if player_hand.get_value() > 21:
                    print("Player busts! Dealer wins!")
                    return
            elif action.lower() == 'stand':
                break

        dealer_hand_value = dealer_hand.get_value()

        while dealer_hand_value < 17:
            dealer_hand.add_card(self.deck.deal_card())
            dealer_hand_value = dealer_hand.get_value()
            print(f"Dealer's hand: {dealer_hand.cards}, Value: {dealer_hand_value}")

        if dealer_hand_value > 21:
            print("Dealer busts! Player wins!")
        elif dealer_hand_value < player_hand.get_value():
            print("Player wins!")
        elif dealer_hand_value == player_hand.get_value():
            print("Push!")
        else:
            print("Dealer wins!")

# fun stuff sam and me added
player = input("What is your name? ").lower()
#Secret Codes/names
if player != "sam":
    print(f"Well why are you on Eli's conputer :raised-eyebrow: {player}!")
elif player == "sam":
    print("You are so cool that you automatically win! :D")
    quit()

if player == "toads are cool":
    print("Somebody knows facts")

if player == "elon musk":
    print("Oooh, how did you find my brother's code?? :D :D ;D")

if player == "hacker":
    print("Oh no")
    quit()
game = BlackjackGame()
game.play()