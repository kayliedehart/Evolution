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

	def parse_situation(self, situation):
		"""
		Reconstruct the JSON input of a situation into a list of
		[attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)]
		and return that list.
		"""
		species_list = []
		for speciesboard in situation:
			if speciesboard:
				s = species.Species()
				s.setFood(speciesboard[0][1])
				s.setBodySize(speciesboard[1][1])
				s.setPopulation(speciesboard[2][1])
				for t in speciesboard[3][1]:
					s.setTraits([trait.Trait(t)])
				species_list.append(s)
			else:
				species_list.append(False)
		return species_list

	def main(self):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)], 
			return a Boolean to stdout whether or not the attack is successful.
		"""
		situation = json.load(sys.argv[1])

		species_list = self.parse_situation(situation)

		test_species = species.Species()

		result = test_species.attackable(species_list)
		
		print result		

if __name__ == "__main__":
	TestHarness()
