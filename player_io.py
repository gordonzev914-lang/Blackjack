from game_logic import dealer_play



def ask_player_action() -> str:
    Player_answer=input("choose H to draw a card and S to Finishe turn")
    if Player_answer==" H":
        return  True
    elif Player_answer=="S":
        return dealer_play()
    else:
        return ask_player_action()