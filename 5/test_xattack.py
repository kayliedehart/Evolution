# Automated unit tests for a xattack test harness for Evolution game
import unittest
import xattack
import difflib
from attack import species
from attack import trait

class TestXAttack(unittest.TestCase):
	"""./xattack.py < test-in.json | diff - 1-out.json"""

  def setUp(self):
    self.spec = species.Species(0,1,1, [])

  def tearDown(self):
    del self.spec
    

  def testMain(self):

if __name__ == '__main__':
    unittest.main()




