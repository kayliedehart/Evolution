import unittest
import ../../5/attack/dealer
import ../../5/attack/species
import ../../5/attack/trait

class TestStrategy(unnittest.TestCase):
  def setUp(self):
    self.player = player.Player()

    self.carnivore = species.Species()
    self.carnivore.setTraits([trait.carnivore])
    self.fat_carnivore = species.Species()
    self.fat_carnivore.setTraits([trait.carnivore])
    self.fat_carnivore.setBodySize(5)

    self.herbavore = species.Species()
    self.fat_herbavore = species.Species()
    self.fat_herbavore.setBodySize(4)

    self.fat_tissue = species.Species()
    self.fat_tissue.setBodySize(3)
    self.fat_tissue.setTraits([trait.fat_tissue])
    self.fat_fat_tissue = species.Species()
    self.fat_fat_tissue.setBodySize(6)
    self.fat_fat_tissue.setTraits([trait.fat_tissue])

    self.opherb = species.Species()
    self.opfatherb = species.Species()
    self.opfatherb.setBodySize(4)
    self.opponent1 = player.Player()
    self.opponent1.setSpeciesBoards([opherb, opfatherb])
    self.opponents = [opponent1]

    self.dealer = dealer.Dealer()
    self.dealer.setListOfPlayers([self.player, self.opponent1])
    self.dealer.setWateringHole(4)

  def tearDown(self):
    self.player
    self.carnivore
    self.herbavore
    self.fat_tissue
    self.opherb
    self.opfatherb
    self.opponent1
    self.opponents
    self.dealer

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
    self.player.setSpeciesBoards([self.herbavore, self.carnivore, self.fat_carnivore])
    self.herbavore.setFood(1)
    self.assertEqual(self.player.feed(self.opponents), (self.fat_carnivore, self.opfatherb))

  def testWontAttackSelf(self):
    self.player.setSpeciesBoards([self.fat_carnivore, self.herbavore])
    self.opponents = []
    self.assertEqual(self.player.feed(self.opponents), False)

if __name__ == '__main__':
    unittest.main()