#实例1-1 一摞有序的纸牌

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')  # nametuple用于构建只有少数属性但是没有方法的对象
print(beer_card)
print("\n")

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])
print("\n")

from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))
print("\n")

print(deck[:3]) # 实现__getitem__方法，变为可迭代
print(deck[12::13])

for card in deck:
    print(card)

print("\n")

# 迭代通常是隐式的，譬如一个集合类型没有实现__contains__方法,那么in运算符就会按顺序做一次迭代搜索
print(Card('Q', 'hearts') in deck)
print(Card("7", 'beasts') in deck)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)