# The Dealer of a 6 Nimmt! game, handles dealing Cards to Players and setting up the Stacks
import components

class Dealer:
	players = [] # list of Players, order matters.
	deck = [] # Contains all remaining cards not in a Stack or held by a Player. At start of game, contains all possible Cards.
	stacks = [] # always contains 4 Stacks

	def __init__(self, players_list):
		self.players = players_list
		for i in range(1, 105):
			self.deck.append(components.Card(i))
		self.shuffleCards()

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
		card = players_card[1]
		stacks_to_pass = []

		def getKey(stack):
			return stack.getCards()[-1].number

		stacks = sorted(self.stacks, key=getKey(), reverse=True)
		for stack in stacks:
			if card.number > stack.getCards()[-1].number:
				if len(stack) < 5:
					stack.setCard(card)
				else:
					stacks_to_pass.append(stack)
					self.removeStack(stack, card)
					break
			else:
				if stack.index() == 3:
					stacks_to_pass = stacks

		return stacks_to_pass

	def removeStack(self, stack, players_card):
		# remove stack Player chose and replace with stack of their card
		return self.stacks

