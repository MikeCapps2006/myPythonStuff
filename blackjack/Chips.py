class Chips:
    
    def __init__(self, bankroll):
        self.bankroll = bankroll

    def win(self, win_amount):
        self.bankroll += win_amount

    def lose(self, lose_amount):
        self.bankroll -= lose_amount
    
    def __str__(self):
        return str(self.bankroll)
    