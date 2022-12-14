from typing import Generator
from random import choice


# ИСПОЛЬЗОВАТЬ: типы параметров и возвращаемое значение должны быть аннотированы
# ДОБАВИТЬ: документацию для функции: строка документации начинается с глагола и в одно предложение отвечает на вопрос "что делает функция?"
def mix_card_deck(deck: list) -> Generator:
    # УДАЛИТЬ: вам не нужен этот список в теле функции генератора — это нивелирует все преимущества генератора, относящиеся к работе с памятью
    shuffled_deck = []

    while deck:
        random_card = choice(deck)
        deck.remove(random_card)
        # УДАЛИТЬ: обновление списка
        shuffled_deck.append(random_card)
        yield random_card


print("Card deck:")
suit = ['chervi', 'bubny', 'piki', 'kresti']

card_deck = []
card_iter = iter(card_deck)
for j in suit:
    for i in range(1, 14):
        card_deck.append((i, j))
        print(next(card_iter))

print("Shuffled deck of cards:")
for card in mix_card_deck(card_deck):
    print(card)


# stdout:
'''Card deck:
(1, 'chervi')
(2, 'chervi')
(3, 'chervi')
(4, 'chervi')
(5, 'chervi')
(6, 'chervi')
(7, 'chervi')
(8, 'chervi')
(9, 'chervi')
(10, 'chervi')
(11, 'chervi')
(12, 'chervi')
(13, 'chervi')
(1, 'bubny')
(2, 'bubny')
(3, 'bubny')
(4, 'bubny')
(5, 'bubny')
(6, 'bubny')
(7, 'bubny')
(8, 'bubny')
(9, 'bubny')
(10, 'bubny')
(11, 'bubny')
(12, 'bubny')
(13, 'bubny')
(1, 'piki')
(2, 'piki')
(3, 'piki')
(4, 'piki')
(5, 'piki')
(6, 'piki')
(7, 'piki')
(8, 'piki')
(9, 'piki')
(10, 'piki')
(11, 'piki')
(12, 'piki')
(13, 'piki')
(1, 'kresti')
(2, 'kresti')
(3, 'kresti')
(4, 'kresti')
(5, 'kresti')
(6, 'kresti')
(7, 'kresti')
(8, 'kresti')
(9, 'kresti')
(10, 'kresti')
(11, 'kresti')
(12, 'kresti')
(13, 'kresti')
Shuffled deck of cards:
(6, 'chervi')
(3, 'kresti')
(2, 'piki')
(10, 'kresti')
(9, 'kresti')
(12, 'bubny')
(4, 'kresti')
(8, 'bubny')
(7, 'kresti')
(10, 'chervi')
(10, 'piki')
(9, 'chervi')
(2, 'bubny')
(8, 'kresti')
(9, 'bubny')
(9, 'piki')
(12, 'chervi')
(12, 'piki')
(6, 'bubny')
(13, 'kresti')
(11, 'piki')
(12, 'kresti')
(7, 'chervi')
(8, 'piki')
(13, 'piki')
(7, 'piki')
(3, 'piki')
(6, 'kresti')
(5, 'piki')
(1, 'bubny')
(1, 'kresti')
(5, 'chervi')
(2, 'chervi')
(13, 'bubny')
(10, 'bubny')
(3, 'chervi')
(8, 'chervi')
(13, 'chervi')
(5, 'kresti')
(11, 'chervi')
(3, 'bubny')
(4, 'piki')
(6, 'piki')
(1, 'chervi')
(11, 'bubny')
(2, 'kresti')
(4, 'chervi')
(1, 'piki')
(4, 'bubny')
(5, 'bubny')
(11, 'kresti')
(7, 'bubny')'''


# ИТОГ: хорошо — 4/5
