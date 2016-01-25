# Implements the protocols between the Player and the rest of the game components of 6 Nimmt!

import components
import dealer
import player

class Main(players):
	players = []
	dealer = None

	def __init__(players):
		players_list = []
		for i in range(players):
			players_list.append(player.Player(i))
		self.players = players_list
		runGame()


	def endOfRound(self):
		for player in self.players:
			# print out points in descending order with player "name"
			if player.bull >= 66:
			else:
				dealer = Dealer(players)
				start_round(self)

	def startRound(self):
		dealer = dealer.Dealer(players_list)
		self.dealer = dealer
		
		for player in players_list:
			player.setHand(dealer.dealFirst())

		dealer.setStacks()

		for player in players_list:
			player.setCurrentStacks(dealer.getStacks())

	def turn(self):
		cards_played
		for player in self.players:
			cards_played.append(player.playCard())




	def runGame(self):

		startRound()

		while len(players_list[0].getHand()) > 0:
			turn()

		endOfRound()
		
		
		
		

