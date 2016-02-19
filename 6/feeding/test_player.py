import unittest
import ../../5/attack/dealer
import ../../5/attack/species
import ../../5/attack/trait

class TestPlayer(unnittest.TestCase):
  def setUp(self):
    self.player = player.Player()

    self.carnivore = species.Species()
    self.carnivore.setTraits([trait.carnivore])

    self.herbavore = species.Species()
    self.herbavore2 = species.Species()

    self.fat_tissue = species.Species()
    self.fat_tissue.setBodySize(3)
    self.fat_tissue.setTraits([trait.fat_tissue])
    self.fat_tissue2 = species.Species()
    self.fat_tissue2.setBodySize(3)
    self.fat_tissue2.setTraits([trait.fat_tissue])

    self.opherb = species.Species()
    self.opfatherb = species.Species()
    self.opfatherb.setBodySize(7)
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

  # Feed Tests
  def testSimpleHerbavore(self):
    self.player.setSpeciesBoards([self.herbavore, self.herbavore2])
    self.assertEqual(self.player.feed(self.opponents), self.herbavore)

  def testSimpleCarnivore(self):
    self.player.setSpeciesBoards([self.carnivore])
    self.assertEqual(self.player.feed(self.opponents), (self.carnivore, self.opherb)

  def testSimpleFatTissue(self):
    self.player.setSpeciesBoards([self.fat_tissue, self.fat_tissue2])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_tissue, 4))

  def testSimpleEmpty(self):
    self.assertEqual(self.player.feed(self.opponents), False)

  def testSimpleFull(self):
    self.carnivore.setFood(1)
    self.herbavore.setFood(1)
    self.player.setSpeciesBoards([self.herbavore, self.carnivore])
    self.assertEqual(self.player.feed(self.opponents), False)

  def testImpossibleCarnivoreAttack(self):
    self.player.setSpeciesBoards([self.carnivore])
    self.opponent1.setSpeciesBoards([self.opfatherb])
    self.assertEqual(self.player.feed(self.opponents), False)

  def testSequencingConstraintOneHungry(self):
    self.player.setSpeciesBoards([self.herbavore])
    with self.assertRaises(Exception("Violation of Sequencing Constraints")):
      self.player.feed(self.opponents)

  def testSequencingConstraintNotEnoughFood(self):
    self.dealer.setWateringHole(0)
    self.player.setSpeciesBoards([self.herbavore])
    with self.assertRaises(Exception("Violation of Sequencing Constraints")):
      self.player.feed(self.opponents)


  # Getter and Setter Tests
  def testGetSetSpeciesBoards(self):
    self.player.setSpeciesBoards(self.herbavore)
    self.assertEqual(self.player.getSpeciesBoards(), self.herbavore)

  def testGetSetAddFoodBag(self):
    self.player.setFoodBag(4)
    self.player.addToFoodBag(1)
    self.assertEqual(self.player.getFoodBag(), 5)

  def testGetSetPlayerID(self):
    self.player.setPlayerId(2)
    self.assertEqual(self.player.getPlayerId(), 2)

if __name__ == '__main__':
    unittest.main()