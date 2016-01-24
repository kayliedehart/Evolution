# The basic components used by the Dealer and Players in 6 Nimmt!

class Card:
	self.number =  # integer in range [1,104]. UNIQUE.
	self.bull =  # integer in range [2,7]

  def getNumber():
    return self.number

  def setNumber(num):
    self.number = num

  def getBullNumber():
    return self.bull

  def setBullNumber(num):
    self.bull = num


class Stack:
  self.cards = []

  def getCards():
    return self.cards

  def setCards(card):
    self.card.append(card)