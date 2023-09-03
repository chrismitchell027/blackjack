import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    
    def reset(self):
        self.cards = []
        self.build()

    def __str__(self):
        card_list = [str(card) for card in self.cards]
        return "\n".join(card_list)
    
class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, card):
        self.cards.append(card)

    def reset(self):
        self.cards = []

    def __str__(self):
        card_list = [f"-> {card}" for card in self.cards]
        return "\n".join(card_list)