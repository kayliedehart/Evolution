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
		self.traits = []

	def getFood(self):
		"""
		Get the number of food tokens of this species.
		"""
		return self.food

	def setFood(self, nat):
		"""
		Update the number of food tokens for this species.
		"""
		if nat < 0:
			raise Exception("Cannot set food to a negative value")
		else:
			self.food = nat

	def addToFood(self, nat):
		"""
		Update the number of food tokens for this species.
		"""
		newFood = self.food + nat
		if newFood < 0:
			raise Exception("Cannot set food to a negative value")
		else:
			self.food = newFood

	def getPopulation(self):
		"""
		Get the current population size for this species.
		"""
		return self.population

	def setPopulation(self, nat):
		"""
		Update the population size of this species.
		"""
		if (nat < 0) or (nat > 7):
			raise Exception("Cannot set population to a negative value or a value greater than 7")
		else:
			self.population = nat

	def addToPopulation(self, nat):
		"""
		Update the population size of this species.
		"""
		newPop = self.population + nat
		if (nat < 0) or (newPop > 7):
			raise Exception("Cannot add a negative value, and cannot set population to a value over 7")
		else:
			self.population = newPop
	
	def getBodySize(self):
		"""
		Get the current body size of this species.
		"""
		return self.bodysize

	def setBodySize(self, nat):
		"""
		Update the body size of this species.
		"""
		if (nat < 0) or (nat > 7):
			raise Exception("Cannot set body size to a negative value or a value greater than 7")
		else:
			self.bodysize = nat

	def getTraits(self):
		return self.traits

	def discardTrait(self, index):
		"""
		Choose a trait in the current set of self.traits to discard.
		"""
		if index > len(self.traits):
			raise Exception("Not a valid index for traits")
		self.traits.pop(index)

	def setTraits(self, lot):
		"""
		Update the set of Traits this species has.
		"""
		for trait in lot:
			if len(self.traits) < MAXTRAITS:
				self.traits.append(trait)
			else:
				#for now, FIFO
				self.discardTrait(0)
				self.traits.append(trait)





