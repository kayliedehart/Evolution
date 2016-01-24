# The Dealer of a 6 Nimmt! game, handles dealing Cards to Players and setting up the Stacks
import components

class Dealer(players_list=None, players_card=None):
	self.players = [] # list of Players, order matters.
	self.deck = [] # Contains all remaining cards not in a Stack or held by a Player. At start of game, contains all possible Cards.
	self.stacks = [] # always contains 4 Stacks

  def getPlayers():
    return self.players

  def setPlayers(group):
    self.players = group

  def addPlayer(player):
    self.players.append(player)

  def getDeck():
    return self.deck

  def setDeck(cards):
    self.deck = cards

  def getStacks():
    return self.stacks

  def setStacks(stacks):
    self.stacks = stacks

	def deal_first(self):
		for player in self.player:
			#pop off the first 10 Cards in self.deck, give as list to Player
		return hand
		
	def make_stacks(self):
		#self.stacks -> 4 lists of one card from self.deck each
		return self.stacks

	def update_stacks(self, players_card):
		# depending on players_card, hand back the necessary stacks
		return self.stacks

