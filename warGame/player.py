class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards) 

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards'
    
    def print_all_cards(self):
        for card in self.all_cards:
            print(card)
        return 'All Cards Printed'