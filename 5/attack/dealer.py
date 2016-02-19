# The Dealer in a game of Evolution
import trait
import species

class Dealer:
	wateringHole = 0
	deck = None
	listOfPlayers = []

	def __init__(self):
		self.wateringHole = 0
		self.listOfPlayers = []

	def setWateringHole(numFoodTokens):
		self.wateringHole = numFoodTokens

	def getWateringHole():
		return self.wateringHole

	def setListOfPlayers(players):
		self.listOfPlayers = players

	def getListOfPlayers():
		return self.listOfPlayers

	def setDeck(deck):
		self.deck = deck

	def getDeck():
		return self.deck