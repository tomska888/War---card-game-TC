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