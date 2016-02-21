import unittest
import dealer
import species
import trait
import strategy
import player

class TestStrategy(unittest.TestCase):
  def setUp(self):
    self.player = player.Player(1, [], 0)

    self.carnivore = species.Species(0, 1, 1, [])
    self.carnivore.setTraits([trait.Trait.carnivore])
    self.fat_carnivore = species.Species(0, 1, 1, [])
    self.fat_carnivore.setTraits([trait.Trait.carnivore])
    self.fat_carnivore.setBodySize(5)

    self.herbavore = species.Species(0, 1, 1, [])
    self.fat_herbavore = species.Species(0, 1, 1, [])
    self.fat_herbavore.setBodySize(4)

    self.fat_tissue = species.Species(0, 1, 1, [])
    self.fat_tissue.setBodySize(3)
    self.fat_tissue.setTraits([trait.Trait.fat_tissue])
    self.fat_fat_tissue = species.Species(0, 1, 1, [])
    self.fat_fat_tissue.setBodySize(6)
    self.fat_fat_tissue.setTraits([trait.Trait.fat_tissue])

    self.opherb = species.Species(0, 1, 1, [])
    self.opfatherb = species.Species(0, 1, 1, [])
    self.opfatherb.setBodySize(4)

    self.opponent1 = player.Player(1, [], 0)
    self.opponent1.setSpeciesBoards([self.opherb, self.opfatherb])
    self.opponents = [self.opponent1]

    self.dealer = dealer.Dealer()
    self.dealer.setListOfPlayers([self.player, self.opponent1])
    self.dealer.setWateringHole(4)

  def tearDown(self):
    del self.player
    del self.carnivore
    del self.herbavore
    del self.fat_tissue
    del self.opherb
    del self.opfatherb
    del self.opponent1
    del self.opponents
    del self.dealer

  def testFatTissueFirst(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_tissue, 4))

  def testBiggestFatTissueFirst(self):
    self.player.setSpeciesBoards([self.fat_tissue, self.fat_fat_tissue])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_fat_tissue, 6))

  def testHerbBeforeCarni(self):
    self.player.setSpeciesBoards([self.herbavore, self.carnivore])
    self.assertEqual(self.player.feed(self.opponents), self.herbavore)

  def testLargestHerbFirst(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_herbavore])
    self.assertEqual(self.player.feed(self.opponents), self.fat_herbavore)

  def testLargestCarnivoreFirstIfAllHerbFed(self):
    self.herbavore.setFood(1)
    self.player.setSpeciesBoards([self.herbavore, self.carnivore, self.fat_carnivore])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_carnivore, self.opfatherb))

  def testWontAttackSelf(self):
    self.player.setSpeciesBoards([self.fat_carnivore])
    self.opponents = []
    self.assertEqual(self.player.feed(self.opponents), False)

if __name__ == '__main__':
    unittest.main()