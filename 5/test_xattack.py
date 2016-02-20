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
    d = difflib.Differ()

  def tearDown(self):
    del self.spec
    del self.d

  def diff(self, expected, output_file):
  	"""
  	Utility for comparing diffs of a given JSON file and a json expression
  	"""
  	for line in outfile.readline():
  		self.d.compare(outfile, json_ex)

	with expected as f1, open(output_file) as f2:
	    differ = Differ()

	    for line in differ.compare(expected.splitlines(True).strip, f2.readlines().strip):
	    	print line
	        
    

  def testMain(self):



if __name__ == '__main__':
    unittest.main()




