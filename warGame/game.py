from deck import Deck
from player import Player

newDeck = Deck()

player_one = Player('Mike')
player_two = Player('Josie')

newDeck.shuffle()

for x in range(26):
    player_one.add_cards(newDeck.deal_one())
    player_two.add_cards(newDeck.deal_one())

def checkForLoss():
    if len(player_one.all_cards) == 0:
        print('Player Two Wins!!!')
        return True
    if len(player_two.all_cards) == 0:
        print('Player One Wins!!!')
        return True
    return False


gameOn = True
roundCount = 0
while gameOn:
    player_one_cards_inPlay = []
    player_two_cards_inPlay = []
    roundCount += 1
    if checkForLoss == True:
        print('game loss')
        gameOn = False
    else:
        print('at war!!!')
        at_war = True
        player_one_cards_inPlay.append(player_one.remove_one())
        player_two_cards_inPlay.append(player_two.remove_one())

        while at_war:
            if player_one_cards_inPlay[0].value() > player_two_cards_inPlay[0].value():
                print('player one wins this duel')
                player_one.add_cards(player_two_cards_inPlay)
                at_war = False
            elif player_two_cards_inPlay[0].value() > player_one_cards_inPlay[0].value():
                print('player two wins this duel')
                player_two.add_cards(player_one_cards_inPlay)
                at_war = False
            else:
                if len(player_one.all_cards) < 5:
                    print('Player two wins!!!')
                    at_war = False
                    gameOn = False
                    break
                if len(player_two.all_cards) < 5:
                    print('Player one wins!!!')
                    at_war = False
                    gameOn = False
                    break
                for x in range(5):
                    print('War in progress. Adding 5 more cards per person')
                    player_one_cards_inPlay.append(player_one.remove_one())
                    player_two_cards_inPlay.append(player_two.remove_one())
print(player_one)
print(player_two)
