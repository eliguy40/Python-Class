# **How to Play**
# 
# 1. Run the game by executing the Python script.
# 2. Add players by calling `add_player()` with their names.
# 3. Start the game by calling `start_game()`.
# 4. Players will be prompted to 'call', 'raise' or 'fold' based on the current state of the pot and their hand 
# value.
# 5. After the flop, turn and river are dealt, players can choose to 'check', 'bet' or 'fold'.
# 6. The game will continue until a player folds or runs out of chips.
# 
# Note: This is a simplified version of Texas Hold'em and does not include features like straddling, bringing-in, 
# or side pots.
# 
# **Game Flow**
# 
# 1. Small blind is posted by the first player to act.
# 2. Big blind is posted by the second player to act.
# 3. Each player is dealt two cards (hole cards).
# 4. Flop is dealt (three community cards).
# 5. Turn is dealt (one more community card).
# 6. River is dealt (final community card).
# 7. Players bet and raise based on their hand value and the current state of the pot.
# 
# **Player Actions**
# 
# 1. Call: match the current bet.
# 2. Raise: increase the current bet.
# 3. Fold: drop out of the game.
# 4. Check: pass action to next player without placing a bet (in case of no bets or raises).
# 5. Bet: place a new bet in the pot.
# 
# **Game End Conditions**
# 
# 1. Player runs out of chips.
# 2. All players fold except one, who is declared the winner.
# 3. Players agree to show their hands and determine the winner based on hand value.

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

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = 1000

    def add_chips(self, amount):
        self.chips += amount

    def remove_chips(self, amount):
        if self.chips >= amount:
            self.chips -= amount
        else:
            print("Not enough chips!")

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.players = []
        self.small_blind = 0
        self.big_blind = 0

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def start_game(self):
        print(f"Blinds: Small - {self.small_blind}, Big - {self.big_blind}")

        for player in self.players:
            action = input(f"{player.name}, do you want to 'call', 'raise' or 'fold'? ")

            if action.lower() == 'call':
                pass
            elif action.lower() == 'raise':
                raise_amount = int(input("How much do you want to raise? "))
                player.remove_chips(raise_amount)
                self.small_blind += raise_amount
                self.big_blind += raise_amount
                print(f"New blinds: Small - {self.small_blind}, Big - {self.big_blind}")
            elif action.lower() == 'fold':
                break

        flop = [self.deck.deal_card(), self.deck.deal_card(), self.deck.deal_card()]
        turn = self.deck.deal_card()
        river = self.deck.deal_card()

        for player in self.players:
            print(f"{player.name}'s hand: {player.hand.cards}")

        action = input("Do you want to 'check', 'bet' or 'fold'? ")

        if action.lower() == 'bet':
            bet_amount = int(input("How much do you want to bet? "))
            player.remove_chips(bet_amount)
            print(f"New pot: {bet_amount}")
        elif action.lower() == 'fold':
            print("Player folds!")

game = Game()
game.add_player("Player 1")
game.add_player("Player 2")

game.start_game()