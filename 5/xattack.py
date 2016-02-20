#!/usr/bin/env python
# a test harness for the attackable method in Dealer for a game of Evolution

from attack import dealer
from attack import trait
from attack import species
from cs4500-aalder-kdehart import parse_json.ParseJSON as parse_json
from cs4500-aalder-kdehart import make_json.MakeJSON as make_json
import sys


class TestHarness:
	def __init__(self):
		self.main()

	def main(self):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)], 
			return a Boolean to stdout whether or not the attack is successful.
		"""
		situation = json.load(sys.argv[1])

		species_list = self.parse_situation(situation)

		test_species = species.Species()

		result = test_species.attackable(species_list)

		print make_json.make_attack(result)

if __name__ == "__main__":
	TestHarness()
