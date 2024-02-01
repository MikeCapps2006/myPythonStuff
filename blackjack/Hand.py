import Card

class Hand:
    def __init__(self):
        self.cards = []  #start with an empty list as we add a card from the Deck class
        self.value = 0   #hand starts at a value of 0
        self.aces = 0    #this keeps track of the aces in the hand

    def add_card(self, card):
        #card passed in is from deck.deal_one --> single Card(suit, rank)
        self.cards.append(card)
        print(card)
        self.value += Card.values[card.rank]

    def adjust_for_aces(self):
        #Adjusts the score if aces are present in the hand self.cards list
        pass

    def __str__(self):
        #Prints out each card in self.cards list
        for card in self.cards:
            print(card)
        return 'End of hand'

""" hand = Hand()
newCard = Card.Card('Hearts', 'Two')
print(newCard)

hand.add_card(newCard)

print(hand) """