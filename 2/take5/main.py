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
					"""
		7. Players pass their self.bull to main
		8. main announces winner of game or creates new Dealer with current list of Players and repeats steps 2-7.
		"""
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
		cards_played = []
		for player in self.players:
			cards_played.append((player.getName(), player.playCard()))

		def getKey(item):
			return item[1]

		cards_played = sorted(cards_played, key=getKey)

		for players_card in cards_played:
			stacks = self.dealer.updateStacks(players_card)
			choice = self.players[players_card[0]].pickStack(stacks)
			self.dealer.removeStack(choice, players_card)

	def runGame(self):

		startRound()

		while len(players_list[0].getHand()) > 0:
			turn()

		endOfRound()

def main():
	Main()

if __name__ == "__main__":
    main()

