from card import Card

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def __str__(self):
        print(self.all_cards)

new_deck = Deck()
print(new_deck)