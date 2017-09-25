#coding=utf-8

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank','suit'])

temp = [0,1,2]+list('ABC')
temp1 = [str(n) for n in range(2,11)]
#print temp1

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(' ')
    
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits 
                                       for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
    
beer_card = Card('7','diamonds')
print beer_card

deck = FrenchDeck()

print deck[0]
print choice(deck)
print
print 


for card in deck:
    print card
    
#获取最上面的3张牌    
print deck[:3]

#获取为的牌
print deck[12::13]

print Card('Q','hearts') in deck 