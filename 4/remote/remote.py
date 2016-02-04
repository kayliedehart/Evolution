#!/usr/bin/env python

# A remote proxy wrapper for a Player in 6 Nimmt!

import socket
import sys
import json
import player

PLAYER_NAME = "Joe"

class RemoteProxyPlayer:
	player = player.Player(PLAYER_NAME)
	last_received = None
	round_in_progress = False

	def start_round(self, lcard):
		"""
		Receives JSON from the server indicating the start of a round and the
		hand dealt to the Player. Passes these cards to the Player and sends 
		back an acknowledgement to the game server
		"""
		self.player.setHand(lcard)
		ack = json.dump(True)
		return ack

	def take_turn(self, stacks):
		"""
		Receives the current stacks in play from the game server and passes them
		to the Player. Returns the Card the Player has chosen to play this turn.
		"""
		players_card = self.player.playCard(stacks)
		players_card = json.dump(players_card)
		return players_card

	def choose(self, stacks):
		"""
		Receives a list of Stacks the Player must choose one of to keep. Returns 
		the chosen Stack. 
		"""
		stack_to_keep = self.player.pickStack(stacks)
		stack_to_keep = json.dump(stack_to_keep)
		return stack_to_keep

	def main(self):
		HOST = ''
		PORT = 45678
		s = None
		for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
		    af, socktype, proto, canonname, sa = res
		    try:
		        s = socket.socket(af, socktype, proto)
		    except socket.error as msg:
		        s = None
		        continue
		    try:
		        s.connect(sa)
		    except socket.error as msg:
		        s.close()
		        s = None
		        continue
		    break
		if s is None:
		    raise Exception('Error: could not open socket')

		data = s.recv()
		message = json.load(data)
		while message:
			if ('start-round' in message) and not round_in_progress:
				ack = self.start_round(message['start-round'])
				s.send(ack)
				round_in_progress = True
			elif 'take-turn' in message:
				if round_in_progress and not ('choose' in message):
					players_card = self.take_turn(message['take-turn'])
					s.send(players_card)
					last_received == 'take-turn'
				else:
					s.send(json.dump(False))
			elif 'choose' in message:
				if round_in_progress and (last_received == 'take-turn') and not ('take-turn' in message):
					stack_to_keep = self.choose(message['choose'])
					s.send(stack_to_keep)
				else:
					s.send(json.dump(False))
			else:
				pass

		#s.close()

if __name__ == "__main__":
    main()