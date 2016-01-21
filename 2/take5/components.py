# The basic components used by the Dealer and Players in 6 Nimmt!

class Card:
	self.number =  # integer in range [1,104]. UNIQUE.
	self.bull =  # integer in range [2,7]

class Stack(cards=None):
	self.cards = cards # list of Cards, order matters. len(self.cards) <= 5
