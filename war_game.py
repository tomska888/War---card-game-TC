import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        if rank.isdigit():
            self.value = int(rank)
        else:
            values = {'J': 11, 'Q': 12, 'K':13, 'A': 14}
            self.value = values[rank]

    def __repr__(self):
        return f"{self.rank}{self.suit}"
    
class Deck:
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_half(self):
        return self.cards[:26], self.cards[26:]