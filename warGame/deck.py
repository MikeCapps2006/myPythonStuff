import card
import random

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)

    def __str__(self):
        for card in self.all_cards:
            print(card)
        return 'End of Deck'

    def shuffle(self):
        random.shuffle(self.all_cards)