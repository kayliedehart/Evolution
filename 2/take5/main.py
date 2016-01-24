# Implements the protocols between the Player and the rest of the game components of 6 Nimmt!

import components
import dealer
import player

def end_of_round(players):
	for player in players:
		# print out points in descending order with player "name"
		if player.bull >= 66:
		else:
			dealer = Dealer(players)
			start_round(self)

def start_round():
	


def main(players):
	"""
	Protocol: 
	1. Create a Dealer, pass in a list of newly generated Players (quantity specified in command line).
	2. Dealer passes 10 cards from Dealer.deck to each Player.
	3. Dealer generates 4 1-Card Stacks (taken from Dealer.deck) and passes a list of those 4 Cards to each Player
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
