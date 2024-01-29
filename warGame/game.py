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
        print('Player one has ran out of cards....Player Two Wins!!!')
        return True
    if len(player_two.all_cards) == 0:
        print('Player two has ran out of cards....Player One Wins!!!')
        return True
    return False


gameOn = True
roundCount = 0
while gameOn:
    roundCount += 1
    player_one_cards_inPlay = []
    player_two_cards_inPlay = []
    roundCount += 1
    if checkForLoss():
        print('game loss')
        print(f'Rounds - {roundCount}')
        gameOn = False
    else:
        at_war = True
        player_one_cards_inPlay.append(player_one.remove_one())
        player_two_cards_inPlay.append(player_two.remove_one())

        while at_war:
            if player_one_cards_inPlay[0].value() > player_two_cards_inPlay[0].value():
                print(player_one_cards_inPlay[0].value())
                print(player_two_cards_inPlay[0].value())
                print('player one wins this duel')
                player_one.add_cards(player_one_cards_inPlay)
                player_one.add_cards(player_two_cards_inPlay)
                at_war = False
            elif player_two_cards_inPlay[0].value() > player_one_cards_inPlay[0].value():
                print('player two wins this duel')
                player_two.add_cards(player_two_cards_inPlay)
                player_two.add_cards(player_one_cards_inPlay)
                at_war = False
            else:
                print('At War!!!')
                print(player_one_cards_inPlay[0])
                print(player_two_cards_inPlay[0])
                if len(player_one.all_cards) < 5:
                    print('Player two wins!!!')
                    print(f'Rounds - {roundCount}')
                    player_two.add_cards(player_one_cards_inPlay)
                    player_two.add_cards(player_one.all_cards)
                    player_one.all_cards = []
                    player_two.add_cards(player_two_cards_inPlay)
                    at_war = False
                    gameOn = False
                    break
                elif len(player_two.all_cards) < 5:
                    print('Player one wins!!!')
                    print(f'Rounds - {roundCount}')
                    player_one.add_cards(player_two_cards_inPlay)
                    player_one.add_cards(player_two.all_cards)
                    player_two.all_cards = []
                    player_one.add_cards(player_one_cards_inPlay)
                    at_war = False
                    gameOn = False
                    break
                else:
                    for x in range(5):
                        print('War in progress. Adding 5 more cards per person')
                        player_one_cards_inPlay.insert(0, player_one.remove_one())
                        player_two_cards_inPlay.insert(0, player_two.remove_one())
print(player_one)
print(player_two)
