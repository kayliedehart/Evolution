#!/usr/bin/env python
# a test harness for the feed method in Player for a game of Evolution

from feeding import player
from feeding import parse_json
from feeding import make_json
import json
import sys


class TestHarness:
	def __init__(self):
		self.main()

	def main(self):
		"""
		Get input from stdin, parse, and get Player's response, parse, and return to stdout
		"""
		feeding = json.load(sys.stdin)

		p_json = parse_json.ParseJSON()
		m_json = make_json.MakeJSON()

		feeding_py = p_json.parse_feeding(feeding)

		if not feeding_py:
			raise Exception("No valid feeding situation received")

		test_player, free_food, players_list = feeding_py

		result = test_player.feed(players_list)

		print m_json.make_meal(result)

if __name__ == "__main__":
	TestHarness()
