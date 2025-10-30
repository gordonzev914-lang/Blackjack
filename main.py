from deck import build_standard_deck
from deck import shuffle_by_sui
from game_logic import calculate_hand_value
from game_logic import deal_two_each
from player_io import ask_player_action
from game_logic import run_full_game


if __name__ == "__main__":
    deck=build_standard_deck()


    shuffled=shuffle_by_suit(deck)



    start=run_full_game(deck,{},{}) 


