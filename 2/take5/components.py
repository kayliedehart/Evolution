# The basic card and stack components for the main components to pass around
import random
from random import randint

class Card:
	number = 0
	bull = 0

	def __init__(self, number):
		self.number = number
		self.bull = self.setBullNumber(False)

	def getNumber(self):
		return self.number

	def getBullNumber(self):
		return self.bull

	def setBullNumber(self, number):
		if not number:
			self.bull = random.randint(2,8)
		else:
			self.bull = number


class Stack:
	cards = []

	def __init__(self, card):
		self.cards.append(card)

	def getCards(self):
		return self.cards

	def setCard(self, card):
		self.cards.append(card)