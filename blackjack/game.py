from Deck import Deck
from Player import Player

print('Welcome to Blackjack')
mike = Player('Mike', 1000)
dealer = Player('Dealer')
deck = Deck()

#deals the first 2 cards each to the player and dealer
def deal_cards():
    mike.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())
    mike.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())

def get_bet_amount():
    global bet_amount
    bet_amount = int(input('How much do you want to bet? \n'))
    return bet_amount

def start_game():
    get_bet_amount()
    deal_cards()

def display_cards():
    print(f"Dealer's Hand:")
    print(f"{dealer.hand}")
    print(f"{mike.name}'s Hand:")
    print(f"{mike.hand}")
    

def check_for_blackjack(player):
    if player.hand.value == 21:
        return True

def compare_hands():
    if mike.hand.value > 21:
        print(f'{mike.name} loses {bet_amount} because he went over')
        mike.chips.lose(bet_amount)
    elif dealer.hand.value > 21:
        print(f'{mike.name} wins {bet_amount} because dealer went over')
        mike.chips.win(bet_amount)
    else:
        if mike.hand.value == dealer.hand.value:
            print('Push!!!')
        elif mike.hand.value > dealer.hand.value:
            print(f'{mike.name} wins {bet_amount} because he said so')
            mike.chips.win(bet_amount)
        else:
            print(f'{mike.name} loses {bet_amount} damn the dealer')
            mike.chips.lose(bet_amount)

def dealer_logic():
    if dealer.hand.value > 16:
        pass
    else:
        while dealer.hand.value < 17:
            dealer.hand.add_card(deck.deal_one())
            display_cards()

gameOn = True
while gameOn:
    start_game()
    display_cards()
    if check_for_blackjack(mike) and check_for_blackjack(dealer):
        print('Push!!!')
    elif check_for_blackjack(mike):
        print(f'{mike.name} wins {bet_amount} credits')
    elif check_for_blackjack(dealer):
        print(f'Dealer has Blackjack!!! {mike.name} loses {bet_amount} credits')
    else:
        player_still_playing = True
        while player_still_playing:
            hit_or_stand = True
            while hit_or_stand:
                another_card = input('Do you want to hit or stand? \n')
                while another_card == 'hit' and mike.hand.value < 21:
                    mike.hand.add_card(deck.deal_one())
                    display_cards()
                    another_card = input('Do you want to hit or stand? \n')
                hit_or_stand = False
                if another_card == 'stand':
                    dealer_logic()
                    print(f'Dealer is standing on {dealer.hand.value}')
                    print(f'{mike.name} is standing on {mike.hand.value}')
                    compare_hands()
                    print(f"{mike.name}'s chip count is {mike.chips}")
                    hit_or_stand = False
                    player_still_playing = False
                else:
                    print('Invalid Response \n')
    play_again = input('Do you want to play again? Yes or No \n').capitalize()
    if play_again == 'No':
        gameOn = False
    else:
        mike.hand.cards = []
        mike.hand.value = 0
        dealer.hand.cards = []
        dealer.hand.value = 0

    




