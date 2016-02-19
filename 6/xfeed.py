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

	def parse_traits(self, traits):
		"""
		Make a list of Traits from a given JSON list of traits
		"""
		trait_list = []
		for trait in traits:
			trait = trait.Trait(trait)
			trait_list.append(trait)
		return trait_list


	def parse_loSpecies(self, LOS):
		"""
		make a list of Species from a JSON LOS. A JSON Species+ is:
			[["food",Nat],
		     ["body",Nat],
		     ["population",Nat],
		     ["traits",LOT]
		     ["fat-food" ,Nat]]
		"""
		species_list = []
		for species in LOS:
			# TODO CONTRACT CHECKING
			this_species = species.Species(species[0], species[1], species[2], self.parse_traits(species[3]))
			if 'fat-tissue' in this_species.getTraits():
				this_species.setFood(species[4])
			species_list.append(this_species)

		return species_list



	def parse_player(self, player):
		"""
		make a Player from a JSON Player. A JSON Player is:
				    [["id",Natural+],
     				["species",LOS],
     				["bag",Natural]]
		"""
		ident = player[0]
		species = self.parse_loSpecies(player[1])
		bag = player[2]

		if (ident > 1) and (bag >= 0):
			return player.Player(ident, species, bag)



	def parse_feeding(self, feeding):
		"""
		Reconstruct the JSON input of a "feeding" into Python: Feeding is [Player, Natural+, LOP]

		"""
		current_player = self.parse_player[feeding[0]]
		free_food = feeding[1]
		all_players = []
		for player in feeding[2]:
			player = self.parse_player(player)
			all_players.append(player)

		return [current_player, free_food, all_players]
		
	
	def encode_decision(self, decision):
		"""
		Translate the Player's feeding decision to json
		"""

	def main(self):
		"""
		Get input from stdin, parse, and get Player's response, parse, and return to stdout
		"""
		situation = json.load(sys.argv[1])

		feeding = self.parse_feeding(feeding)

		test_player, free_food, players_list = feeding

		result = test_player.feed(players_list)

		print result		

if __name__ == "__main__":
	TestHarness()
