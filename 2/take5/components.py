# The basic components used by the Dealer and Players in 6 Nimmt!
from random import randint

class Card:
	self.number =  0
	self.bull =  0
  
  def __init__(number):
  	self.number = number
  	self.bull = randint(2,8)

  def getNumber(self):
    return self.number

  def getBullNumber(self):
    return self.bull


class Stack:
  self.cards = []

  def __init__(card):
  	self.cards.append(card)

  def getCards(self):
    return self.cards

  def setCards(self, card):
    self.cards.append(card)