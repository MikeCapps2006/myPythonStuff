import Card

class Hand:
    def __init__(self):
        self.cards = []  #start with an empty list as we add a card from the Deck class
        self.value = 0   #hand starts at a value of 0
        self.aces = 0    #this keeps track of the aces in the hand

    def add_card(self, card):
        #card passed in is from deck.deal_one --> single Card(suit, rank)
        self.cards.append(card)
        self.value += Card.values[card.rank]

        #track aces
        if(card.rank) == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        #Adjusts the score if aces are present in the hand self.cards list
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        #Prints out each card in self.cards list
        for card in self.cards:
            print(card)
        return f'Value: {self.value}'

""" hand = Hand()
newCard = Card.Card('Hearts', 'Two')
print(newCard)

hand.add_card(newCard)

print(hand) """