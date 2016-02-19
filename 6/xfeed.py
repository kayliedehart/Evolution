#!/usr/bin/env python
# a test harness for the feed method in Player for a game of Evolution

from 5/attack import trait
from 5/attack import species
from feeding import player
import sys
import json


class TestHarness:
	def __init__(self):
		self.main()

	def parse_feeding(self, feeding):
		"""
		Reconstruct the JSON input of a "feeding" into Python: Feeding is [Player, Natural+, LOP]; 
		Player is  [["id",Natural+],
     				["species",LOS],
     				["bag",Natural]]

		"""

	
	def encode_decision(self, decision):
		"""
		Translate the Player's feeding decision to json
		"""

	def main(self):
		"""
		Get input from stdin, parse, and get Player's response, parse, and return to stdout
		"""
		situation = json.load(sys.argv[1])

		species_list = self.parse_feeding(feeding)

		test_player = player.Player()

		result = test_player.feed(species_list)

		print result		

if __name__ == "__main__":
	TestHarness()
