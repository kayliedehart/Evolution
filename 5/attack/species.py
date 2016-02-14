# A Species (Species board) for the game Evolution

import trait
from random import randint

MAXTRAITS = 3

class Species:
	food = 0
	population = 1
	bodysize = 0
	traits = []

	def __init__(self):
		self.food = 0
		self.population = 1
		self.bodysize = 0

	def getFood(self):
		"""
		Get the number of food tokens of this species.
		"""
		return self.food

	def setFood(self, nat):
		"""
		Update the number of food tokens for this species.
		"""
		self.food += nat

	def getPopulation(self):
		"""
		Get the current population size for this species.
		"""
		return self.population

	def setPopulation(self, nat):
		"""
		Update the population size of this species.
		"""
		self.population += nat

	def getBodySize(self):
		"""
		Get the current body size of this species.
		"""
		return self.bodysize

	def setBodySize(self, nat):
		"""
		Update the body size of this species.
		"""
		self.bodysize += nat

	def getTraits(self):
		return self.traits

	def discardTrait(self, index):
		"""
		Choose a trait in the current set of self.traits to discard.
		"""
		# for now, just get rid of a random trait. Eventually prompt player.
		index = randint(MAXTRAITS+1)
		self.traits.pop(index)

	def setTraits(self, lot):
		"""
		Update the set of Traits this species has.
		"""
		for trait in lot:
			if len(self.traits) < MAXTRAITS:
				self.traits.append(trait)
			else:
				self.discardTrait()
				self.traits.append(trait)





