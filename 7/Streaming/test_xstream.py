# unit tests for EchoStream's validate method
import unittest

class TestSpecies(unittest.TestCase):

  def setUp(self):
    self.frag1 = 3
    self.frag2 = [1, 3, 5]
    self.frag3 = {"cookies" : 246}
    self.frag4 = "Felleisen"
    self.frag5 = {}

  def tearDown(self):
    del self.frag1
    del self.frag2
    del self.frag3
    del self.frag4

  def testValidate1(self):

  def testValidate2(self):

  def testValidate3(self):

  def testValidate4(self):

  def testValidate5(self):

  def testValidate6(self):
    
    

if __name__ == '__main__':
    unittest.main()
