# Create JSON representations of Evolution python objects

import trait
import species
import player
import dealer
import json


class MakeJSON:

	def make_speciesPlus(self, species):
		"""
		Construct a string in the format of a JSON Species+
		"""
		str_species = ('[["food",{}],["body",{}],["population",{}],["traits",[{}]]'.format(species.getFood(),
																						   species.getBodySize(),
																						   species.getPopulation(),
																						   species.getTraits()))
		if "fat-tissue" in species.getTraits():
			###### FUCKING SHIT DO WE NEED TO KEEP TRACK OF THIS IN RETURNS?
			str_species + "['fat-food',{}]]".format((0))
		else:
			str_species + "]"
		return str_species

	def make_player(self, player):
		"""
		Construct a string in the format of a JSON Player
		"""
		str_player = "[['id',{}],".format(player.getPlayerId())
		for species in player.getSpeciesBoards():
			str_player + self.make_speciesPlus
		str_player + "['bag',{}]]".format(player.getFoodBag())
		return str_player

	def make_meal(self, feeding_out):
		"""
		Construct a JSON message to describe a player's feeding decision.
		The output is one of:
			false,
			Species+,
			[Species+, Nat],
			[Species+, Player, Species+]
		"""
		if not feeding_out:
			return json.dump(False)
		if len(feeding_out) == 1:
			return json.dumps(self.make_speciesPlus(feeding_out))
		else:
			meal = "["
			for item in feeding_out:
				if type(item) == species.Species:
					meal + self.make_speciesPlus(item))
				elif type(item) == int:
					meal + "," + str(int)
				elif type(item) == player.Player:
					meal + "," + (self.make_player(item)) + ","
			meal + "]"
		return json.dumps(meal)

	def make_attack(self, attack):
		"""
		Construct a JSON message to describe the result of an species' attack scenario (Boolean)
		"""
		return json.dumps(attack)