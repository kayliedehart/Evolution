# The basic components used by the Dealer and Players in 6 Nimmt!
from random import randint

class Card:
	number =  0
	bull =  0

	def __init__(self, number):
		self.number = number
		self.bull = setBullNumber()

	def getNumber(self):
		return self.number

	def getBullNumber(self):
		return self.bull

	def setBullNumber(self, card):
		if not card:
			self.bull = randint(2,8)
		else:
			self.bull = card


class Stack:
	cards = []

	def __init__(self, card):
		self.cards.append(card)

	def getCards(self):
		return self.cards

	def setCards(self, card):
		self.cards.append(card)