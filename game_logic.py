from player_io import ask_player_action



def calculate_hand_value(hand: list[dict])-> int :
    rank_value_list=[{'2':2},{'3':3},{'4':4},{'5':5},{'6':6},{'7':7},{'8':8},{'9':9},{'10':10},{'J':10},{'Q':10},{'K':10},{'A':1}]
    hand_value=0
    for dict in hand:
        for key in dict:
            for i in rank_value_list:
                for j in i:
                    if j==dict[key]:
                        hand_value+=i[j]
    return int(hand_value)
# print(calculate_hand_value(({'rank': '10', 'suite': 'S'}, {'rank': 'J', 'suite': 'S'}, {'rank': 'Q', 'suite': 'S'})))
                



def deal_two_each(deck: list[dict], player: dict, dealer: dict):
    player[0]=deck.pop()
    player[1]=deck.pop()
    
    dealer[0]=deck.pop()
    dealer[1]=deck.pop()
    
    print(player)
    print(dealer)
    # player_cards=[]
    # for i in player:
    #     for j in player[i]:
    #         player_cards.append(j)
    # print(player_cards)        

    # player_value=calculate_hand_value(player)
    # print(f" thes is the initial value of the players hand{ player_value}")
    # dealer_value=calculate_hand_value(dealer)
    # print(f" thes is the initial value of the dealers hand{ dealer_value}")
    
print(deal_two_each([{'rank': '2', 'suite': 'H'}, {'rank': '3', 'suite': 'H'}, {'rank': '4', 'suite': 'H'}, {'rank': '5', 'suite': 'H'}, {'rank': '6', 'suite': 'H'}, {'rank': '7', 'suite': 'H'}, {'rank': '8', 'suite': 'H'}, {'rank': '9', 'suite': 'H'}],{},{}))
    


def dealer_play(deck: list[dict], dealer: dict) -> bool:
      






def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None: 
    players_chicie=ask_player_action()
        if players_chicie== True:
            player[2]=deck.pop()
            hand_value+=calculate_hand_value(player[2])
            if hand_value<21:
                print("player lost")
            else:
                players_chicie()    
        if players_chicie=="S":
           the_dealer=dealer_play()
           if the_dealer==True:
               the_dealer()
            else:
               print ("end game")
                  

    