# handles JSON parsing for the game Evolution

import trait
import species
import player
import dealer
import json


class ParseJSON:

	def __init__(self):
		pass

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
			this_species = species.Species(species[0][1], species[1][1], species[2][1], self.parse_traits(species[3][1]))
			if (trait.Trait.fat_tissue in this_species.getTraits()) and species[4]:
				this_species.setFood(species[4][1])
			species_list.append(this_species)

		return species_list



	def parse_player(self, player):
		"""
		make a Player from a JSON Player. A JSON Player is:
				    [["id",Natural+],
     				["species",LOS],
     				["bag",Natural]]
		"""
		ident = player[0][1]
		species = self.parse_loSpecies(player[1][1])
		bag = player[2][1]

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