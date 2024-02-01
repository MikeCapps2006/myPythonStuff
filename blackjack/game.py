from Deck import Deck
from Player import Player

gameOn = True
while gameOn:
    newDeck = Deck()
    mike = Player('Mike', 1000)

    mike.hand.add_card(newDeck.deal_one())
    print(mike)
    print(mike.hand.value)
    gameOn = False


