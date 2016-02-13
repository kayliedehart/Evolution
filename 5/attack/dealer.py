# The Dealer in a game of Evolution

class Dealer:

	def __init__(self):
		

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




	 # situation = [carnivore, [],] -> True
	 #    s2 = no traits, no traits -> None
	 #    s3 = carnivore, burrowing -> False
	 #    s4 = carnivore climbing, climbing -> True
	 #    s5 = carnivore climbing, burrowing -> False
	 #    s6 = carnivore, symbiosis body ==1, body ==2 -> False
	 #    s7 = carnivore, symbiosis body ==2, body == 1 -> True
	 #    s8 = carnivore, none, warning_call -> False
	 #    s9 = carnivore ambush, none, warning_call -> True
	 #    s10 = carnivore pack_hunting popSize==3, herding popSize==5 -> True
	 #    s11 = carnivore pack_hunting popSize==3, herding popSize==6 -> False
	 #    s12 = carnivore, burrowing foodTokens==5 popSize==5 -> False
	 #    s13 = carnivore, burrowing foodTokens==4 popSize==5 -> True
	 #    s14 = carnivore body==5, hard_shell body==2 -> False
	 #    s15 = carnivore body==5, hard_shell body==1 -> True

	 #    s16 = attacker == defender -> None
    

