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
        SUITS = ['♠', '♥', '♦', '♣']
        RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_half(self):
        return self.cards[:26], self.cards[26:]
    
class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.round_count = 0
        self.deck = Deck()
        self.deck.shuffle()
        half1, half2 = self.deck.deal_half()
        self.player1.hand = half1
        self.player2.hand = half2

    def play_round(self):
        self.round_count += 1
        print(f"\nRound {self.round_count}:")

        if not self.player1.has_cards():
            print(f"{self.player1.name} win the game!")
            return False
        if not self.player2.has_cards():
            print(f"{self.player2.name} win the game!")
            return False
        
        card1 = self.player1.play_card()
        card2 = self.player2.play_card()
        print(f"{self.player1.name} plays {card1}, {self.player2.name} plays {card2}")

        if card1.value > card2.value:
            print(f"{self.player1.name} wins the round!")
            self.player1.collect_card([card1,card2])
        elif card2.value > card1.value:
            print(f"{self.player2.name} wins the round!")
            self.player2.collect_card([card1,card2])
        else:
            print(f"It's a tie! War begins!")
            
        return True

    def play_game(self):
        print("Start the game!")
        while self.play_game():
            pass
        print("Game over!")


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self):
        if self.hand:
            return self.hand.pop(0)
        return None

    def has_cards(self):
        return len(self.hand) > 0
    
    def collect_card(self, cards):
        self.hand.extend(cards)

    def __str__(self):
        return f"{self.name} (Cards left: {len(self.hand)})"


if __name__ == "__main__":
    game = Game("Player 1", "Player 2")
    game.play_game()
