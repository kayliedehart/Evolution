#!/usr/bin/env python
# a test harness for the attackable method in Dealer for a game of Evolution

from attack import dealer
from attack import trait
from attack import species
import sys
import json


class TestHarness:
	def __init__(self):
		self.main()

	def main(self):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)], 
			return a Boolean to stdout whether or not the attack is successful.
		"""
		with open(sys.argv[1], 'r') as f:
			situation = json.load(f)
			f.close()

		species_list = []
		for speciesboard in situation:
			if speciesboard:
				s = species.Species()
				s.setFood(speciesboard[0][1])
				s.setBodySize(speciesboard[1][1])
				s.setPopulation(speciesboard[2][1])
				s.setTraits(speciesboard[3][1])
				species_list.append(s)
			else:
				species_list.append(False)


		new_dealer = dealer.Dealer()

		result = new_dealer.attackable(species_list)
		sys.stdout = open(sys.argv[2], 'w')
		print result		

if __name__ == "__main__":
	TestHarness()
