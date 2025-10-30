
['2','3','4','5','6','7','8','9','10','J','Q','K','A']
['H','C','D','S']


def build_standard_deck(list_of_ranks,list_of_suites,deck_of_cards=[]):
    for i in list_of_suites:
        for j in list_of_ranks:
            deck_of_cards.append({"rank":j,"suite":i})
    return deck_of_cards

print(build_standard_deck(['2','3','4','5','6','7','8','9','10','J','Q','K','A'],['H','C','D','S']))

    























def shuffle_by_suit(deck: list[dict], swaps: int = 5000):
    pass
