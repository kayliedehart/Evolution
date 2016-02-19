# unit tests for a xattack test harness for Evolution game
import unittest
import xattack
from attack import species
from attack import trait

class TestXAttack(unittest.TestCase):
	"""./xattack.py < test-in.json | diff - 1-out.json"""

  def setUp(self):
    self.spec = species.Species()

  def tearDown(self):
    del self.spec

  def testParseSituation(self):
    

  def testMain(self):

if __name__ == '__main__':
    unittest.main()




