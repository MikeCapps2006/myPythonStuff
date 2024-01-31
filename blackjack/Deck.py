import Card
import random

class Deck:
    
    def __init__(self):
        self.all_cards = []

        for rank in Card.ranks:
            for suit in Card.suits:
                created_card = Card.Card(suit, rank)
                self.all_cards.append(created_card)
        random.shuffle(self.all_cards)

    def __str__(self):
        print(f'Length of deck: {len(self.all_cards)}')
        for card in self.all_cards:
            print(card)
        return 'End of Deck'

    def deal_one(self):
        return self.all_cards.pop(0)

