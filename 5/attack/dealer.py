# The Dealer in a game of Evolution

class Dealer:

	def attackable(self, situation):
			"""
			Checks to see if an attack is successful in the given Situation.
			A Situation is [defender:Species, attacker:Species, (optional neighbor:Species, neighbor:Species)]
			Returns a Boolean. 
			"""
			defender, attacker, neighbor1, neighbor2 = situation
			if 'carnivore' in attacker.getTraits():
				if 'carnivore' in defender.getTraits():
					return False
				else: 
					# There is a metric fuckton to do here, I just want it to be valid Python for now
					return True
			else:
				raise Exception("Attacking Species must be a carnivore")