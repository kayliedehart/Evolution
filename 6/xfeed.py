#!/usr/bin/env python
# a test harness for the feed method in Player for a game of Evolution

from 5/attack import trait
from 5/attack import species
from feeding import player
from cs4500-aalder-kdehart import parse_json.ParseJSON as parse_json
import sys
import json


class TestHarness:
	def __init__(self):
		self.main()
		
	
	def encode_decision(self, decision):
		"""
		Translate the Player's feeding decision to json
		"""
		return true

	def main(self):
		"""
		Get input from stdin, parse, and get Player's response, parse, and return to stdout
		"""
		situation = json.load(sys.argv[1])

		feeding = parse_json.parse_feeding(feeding)

		test_player, free_food, players_list = feeding

		result = test_player.feed(players_list)

		print result		

if __name__ == "__main__":
	TestHarness()
