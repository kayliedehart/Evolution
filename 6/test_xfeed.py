# Automated unit tests for the test harness for the Player's feed method
import unittest
import xfeed
import difflib
from 5/attack import species
from 5/attack import trait

class TestXFeed(unittest.TestCase):
	"""./xfeed.py < test-in.json | diff - 1-out.json
	"""

  def setUp(self):
    self.spec = species.Species(0, 1, 1, [])

  def tearDown(self):
    del self.spec
    

  def testMain(self):
  	

if __name__ == '__main__':
    unittest.main()
