import unittest
import ../../5/attack/dealer
import ../../5/attack/species
import ../../5/attack/trait

class TestPlayer(unnittest.TestCase):
  def setUp(self):
    self.carnivore = species.Species(0, 1, 1, [])
    self.carnivore.setTraits([trait.carnivore])
    self.herbavore = species.Species(0, 1, 1, [])
    self.fat_tissue = species.Species(0, 1, 1, [])
    self.fat_tissue.setTraits([trait.fat_tissue])

  def tearDown(self):
    self.carnivore
    self.herbavore
    self.fat_tissue

  def testHerbavore(self):
    self.assertEqual()

if __name__ == '__main__':
    unittest.main()