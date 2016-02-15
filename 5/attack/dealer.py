# The Dealer in a game of Evolution
import trait

class Dealer:
	wateringHole = []
	deck = None

	def __init__(self):
		self.wateringHole = []

	def neighborsHelp(self, neighbors):
		"""
		Returns boolean value for if a Species' neighbors can help prevent an attack, 
		given a list of neighboring Species
		"""
		for neighbor in neighbors:
			if warning_call in neighbor.traits:
				return True
		return False

	def canBurrow(self, defender):
		"""
		Returns boolean whether a defender can successfully use burrowing
		"""
		if defender.getFood() >= defender.getPopulation():
			return True
		else:
			return False

	def goodSymbiosis(self, defender, neighborRight):
		"""
		Returns whether symbiosis helps the defender avoid attack, ie:
		if the neighbor to their right has a larger body size then the defender
		"""
		if defender.getBodySize() < neighborRight.getBodySize():
			return True
		else:
			return False

	def blockingShell(self, attacker, defender):
		"""
		Returns whether a defender with hard_shell can defend against their attacker
		"""
		if (attacker.getBodySize() - defender.getBodySize()) <= 3:
			return True
		else:
			return False

	def herdingHelp(self, attacker, defender):
		"""
		Returns whether a defender with herding can successfully block an attacker
		"""
	 	attackers_popsize = attacker.getPopulation()
		if pack_hunting in attacker.traits:
			attackers_popsize += attacker.getBodySize()

		if attackers_popsize <= defender.getPopulation():
			return True
		else:
			return False

		

	def attackable(self, situation):
			"""
			Checks to see if an attack is successful in the given Situation.
			A Situation is [defender:Species, attacker:Species, (optional neighbor:Species, neighbor:Species)]
			Returns a Boolean. 
			"""
			attacker, defender, neighborLeft, neighborRight = situation
			neighbors = [neighborLeft, neighborRight]
			if trait.Offensive.carnivore in attacker.traits:
				if defender.getPopulation() == 0:
					return False
				if (trait.Offensive.ambush not in attacker.traits) and self.neighborsHelp(neighbors):
					return False
				elif climbing in defender.traits and climbing not in attacker.traits:
					return False
				elif burrowing in defender.traits and self.canBurrow(defender):
					return False
				elif symbiosis in defender.traits and self.goodSymbiosis(defender, neighborRight):
					return False
				elif hard_shell in defender.traits and self.blockingShell(attacker, defender):
					return False
				elif herdingHelp in defender.traits and self.herdingHelp(attacker, defender):
					return False
				elif attacker == defender:
					raise Exception("A species cannot attack itself")
				else:
					return True
			else:
				raise Exception("Attacking Species must be a carnivore")


