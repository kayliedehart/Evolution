import unittest
import dealer
import species
import trait

class TestDealer(unittest.TestCase):
  def setUp(self):
    self.dealer = dealer.Dealer()
    self.attacker = species.Species()
    self.defender = species.Species()
    self.neighborleft = species.Species()
    self.neighborright = species.Species()

  def tearDown(self):
    del self.dealer
    del self.attacker
    del self.defender
    del self.neighborleft
    del self.neighborright

  def testAttackableBothEmpty(self):
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), None)

  def testAttackableCarnivoreBasic(self):
    self.attacker.setTraits([trait.Offensive.carnivore])
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), True)

  def testAttackableClimbing(self):
    self.attacker.setTraits([trait.Defensive.climbing])
    self.defender.setTraits([trait.Defensive.climbing])
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), False)

  def testAttackableNotClimbing(self):
    self.defender.setTraits([trait.Defensive.climbing])
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), True)

  def testSymbiosis(self):
    self.defender.setTraits([trait.Aid.symbiosis])
    self.defender.setBodySize(1)
    self.neighborright.setBodySize(2)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender, None, self.neighborright]), False)

  def testBadSymbiosis(self):
    self.defender.setTraits([trait.Aid.symbiosis])
    self.defender.setBodySize(2)
    self.neighborright.setBodySize(1)
    self.neighborleft.setBodySize(4)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender, self.neighborleft, self.neighborright]), True)

  def testWarningCall(self):
    self.neighborright.setTraits([trait.Aid.warningCall])
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender, self.neighborleft, self.neighborright]), False)

  def testAmbush(self):
    self.attacker.setTraits([trait.Offensive.ambush])
    self.neighborright.setTraits([trait.Aid.warningCall])
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender, self.neighborleft, self.neighborright]), True)

  def testPackHunting(self):
    self.attacker.setTraits([trait.Offensive.pack_hunting])
    self.attacker.setPopulation(3)
    self.defender.setPopulation(5)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), True)

  def testFailPackHunting(self):
    self.attacker.setTraits([trait.Offensive.pack_hunting])
    self.attacker.setPopulation(3)
    self.defender.setPopulation(6)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), False)

  def testBurrowing(self):
    self.defender.setFood(5)
    self.defender.setPopulation(5)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), True)

  def testFailBurrowing(self):
    self.defender.setFood(4)
    self.defender.setPopulation(5)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), False)

  def testHardShell(self):
    self.attacker.setBodySize(5)
    self.defender.setBodySize(2)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), False)

  def testFailHardShell(self):
    self.attacker.setBodySize(5)
    self.defender.setBodySize(1)
    self.assertEqual(self.dealer.attackable([self.attacker, self.defender]), True)

  def testAttackerAttacksSelf(self):
    self.assertEqual(self.dealer.attackable([self.attacker, self.attacker]), None)

if __name__ == '__main__':
    unittest.main()