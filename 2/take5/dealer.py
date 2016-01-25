# The Dealer of a 6 Nimmt! game, handles dealing Cards to Players and setting up the Stacks
import components

class Dealer(players_list, players_card):
	self.players = [] # list of Players, order matters.
	self.deck = [] # Contains all remaining cards not in a Stack or held by a Player. At start of game, contains all possible Cards.
	self.stacks = [] # always contains 4 Stacks

	def __init__(self, players_list):
		self.players = players_list
		for i in range(1, 105):
			self.deck.append(components.Card(i))
		shuffleCards()

	def getPlayers(self):
		return self.players

	def setPlayers(self, group):
		self.players = group

	def addPlayer(self, player):
		self.players.append(player)

	def getDeck(self):
		return self.deck

	def setDeck(self, cards):
		self.deck = cards

	def getStacks(self):
		return self.stacks

	def setStacks(self):
		stacks = []
		for i in range(1,5):
			stacks.append(components.Stack(self.deck.pop(1)))
		self.stacks = stacks

	def shuffleCards(self):
		# reset the deck to be in random order

	def dealFirst(self):
		hand = self.deck.pop(10)
		return hand
	
	def updateStacks(self, players_card):
		# depending on players_card, hand back the necessary stacks

	def removeStack(self, stack, players_card):
		# remove stack Player chose and replace with stack of their card
		return self.stacks

