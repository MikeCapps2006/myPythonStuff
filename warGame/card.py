class Card:
    suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
    rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        output = self.rank + ' of ' + self.suit
        print(output)
        return output