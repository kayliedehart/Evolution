# unit tests for a Species in the game Evolution

class TestSpecies(unittest.TestCase):

  def setUp(self):
    self.spec = species.Species()

  def tearDown(self):
    del self.spec

  def testSetAndGetFood(self):
    self.spec.setFood(3)
    self.spec.addToFood(1)
    self.assertEqual(self.spec.getFood(), 4)

  def testSetAndGetPopulation(self):
    self.spec.setPopulation(4)
    self.spec.addToPopulation(1)
    self.assertEqual(self.spec.getPopulation(), 5)

  def testSetAndGetBodySize(self):
    self.spec.setBodySize(2)
    self.assertEqual(self.spec.getBodySize(), 2)

  def testSetAndGetTraits(self):
    self.spec.setTraits([Offensive.carnivore])
    self.assertEqual(self.spec.getTraits(), [Offensive.carnivore])
    self.spec.discardTraits(0)
    self.assertEqual(self.spec.getTraits(), None)

if __name__ == '__main__':
    unittest.main()




