# Implements the protocols between the Player and the rest of the game components of 6 Nimmt!

import components
import dealer
import player

class Main:
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
			"""
		4. Each Player passes 1 card to the Dealer
		5.1. Dealer gives Player with smallest Card.number the updated Stacks according to the Player's Card;
			-If the Player's Card can be placed without penalty, return an empty list
			-If the Player's Card results in an overflow (more than 5 cards in a Stack), pass that Stack to Player and update Stack with Player's Card
			-If the Player's Card is smaller than all top Cards, return a list of all Stacks to the Player
				5.2. Player indicates to Dealer which Stack they're keeping
			Dealer moves on and repeats step 5.1 with Player with next smallest Card.number until all Cards have been placed
		6. Repeat steps 4 and 5 until Players are out of Cards
		7. Players pass their self.bull to main
		8. main announces winner of game or creates new Dealer with current list of Players and repeats steps 2-7.
		"""


	def runGame(self):

		startRound()

		while len(players_list[0].getHand()) > 0:
			turn()

		endOfRound()

		


