# The Dealer of a 6 Nimmt! game, handles dealing Cards to Players and setting up the Stacks

class Dealer(players_list=None, players_card=None):	
	self.players = [] # list of Players, order matters.
	self.deck = [] # Contains all remaining cards not in a Stack or held by a Player. At start of game, contains all possible Cards.
	self.stacks = [] # always contains 4 Stacks
