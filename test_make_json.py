# unit tests for make_json for Evolution
from 5/attack import trait
from 5/attack import species
from 6/feeding import player
from 5/attack import dealer
import json
import unittest

class TestMakeJSON(unittest.TestCase):

	def setUp(self):
		self.spec = species.Species()
		

	def tearDown(self):
		del self.spec
	

	def test_parseSituation(self):

	def test_parseTraits(self):
		
	def test_parseLoSpecies(self):
	
	def test_parsePlayer(self):
		
	def test_parseFeeding(self):
		


if __name__ == '__main__':
	unittest.main()