#!/usr/bin/env python
# a test harness for the attackable method in Dealer for a game of Evolution

import dealer
import sys
import json

class TestHarness:
	def __init__(self):
		self.main()

	def main(self):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)], 
			return a Boolean to stdout whether or not the attack is successful.
		"""
		situation = sys.argv
		print situation

		new_dealer = dealer.Dealer()

		print "created a dealer"
		result = new_dealer.attackable(situation)
		print result		

if __name__ == "__main__":
	TestHarness()
