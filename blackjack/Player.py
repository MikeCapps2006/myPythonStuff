import Hand
import Chips

class Player:
    
    def __init__(self, name, chips = 1000):
        self.name = name
        self.chips = Chips.Chips(chips)
        self.hand = Hand.Hand()

    def __str__(self):
        print(f"{self.name} has {len(self.hand.cards)} cards and has {self.chips} chips")
        print(f"{self.hand}")
        return 'End of Player'