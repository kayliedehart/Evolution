#!/usr/bin/env python
# a test harness for the feed method in Player for a game of Evolution

from feeding import player
from feeding import parse_json
from feeding import make_json
import sys


class TestHarness:
	def __init__(self):
		self.main()

	def main(self):
		"""
		Get input from stdin, parse, and get Player's response, parse, and return to stdout
		"""
		situation = json.load(sys.stdin)

		parse_json = parse_json.ParseJSON()
		make_json = make_json.MakeJSON()

		feeding = parse_json.parse_feeding(feeding)

		test_player, free_food, players_list = feeding

		result = test_player.feed(players_list)

		make_json.make_meal(result)

if __name__ == "__main__":
	TestHarness()
