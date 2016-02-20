# Create JSON representations of Evolution python objects

from 5/attack import trait
from 5/attack import species
from feeding import player
from attack import dealer
import json


class MakeJSON:
	def make_meal(self, feeding_out):
		"""
		Construct a JSON message to describe a player's feeding decision
		"""
		return json.dumps(meal)

	def make_attack(self, attack):
		"""
		Construct a JSON message to describe the result of an species' attack scenario
		"""
		return json.dumps(attack)