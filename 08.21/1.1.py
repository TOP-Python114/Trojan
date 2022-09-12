from random import choice
suit = ['chervi', 'bubny', 'piki', 'kresti']

card_deck = []
card_iter = iter(card_deck)
for j in suit:
    for i in range(1, 14):
        card_deck.append((i, j))
        print(next(card_iter))

def mix_card_deck(deck):
    shuffled_deck = []

    while deck:
        random_card = choice(deck)
        deck.remove(random_card)
        shuffled_deck.append(random_card)
        yield random_card

for card in mix_card_deck(card_deck):
    print(card)


