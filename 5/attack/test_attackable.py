import unittest
import species
import trait

class testAttackable(unittest.TestCase):
  def setUp(self):
    self.species = species.Species()
    self.attacker = species.Species()
    self.attacker.setTraits([trait.Trait.carnivore])
    self.defender = species.Species()
    self.neighborleft = species.Species()
    self.neighborright = species.Species()

  def tearDown(self):
    del self.species
    del self.attacker
    del self.defender
    del self.neighborleft
    del self.neighborright

  def testAttackableBothEmpty(self):
    self.attacker.discardTrait(0)
    with self.assertRaises(Exception("Attacking Species must be a carnivore")):
      self.species.attackable([self.attacker, self.defender, False, False])

  def testAttackableCarnivoreBasic(self):
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), True)

  def testAttackableClimbing(self):
    self.attacker.setTraits([trait.Trait.climbing])
    self.defender.setTraits([trait.Trait.climbing])
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), True)

  def testAttackableNotClimbing(self):
    self.defender.setTraits([trait.Trait.climbing])
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), False)

  def testSymbiosis(self):
    self.defender.setTraits([trait.Trait.symbiosis])
    self.defender.setBodySize(1)
    self.neighborright.setBodySize(2)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, self.neighborright]), False)

  def testBadSymbiosis(self):
    self.defender.setTraits([trait.Trait.symbiosis])
    self.defender.setBodySize(2)
    self.neighborright.setBodySize(1)
    self.neighborleft.setBodySize(4)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, self.neighborleft, self.neighborright]), True)

  def testWarningCall(self):
    self.neighborright.setTraits([trait.Trait.warning_call])
    self.assertEqual(self.species.attackable([self.attacker, self.defender, self.neighborleft, self.neighborright]), False)

  def testAmbush(self):
    self.attacker.setTraits([trait.Trait.ambush])
    self.neighborright.setTraits([trait.Trait.warning_call])
    self.assertEqual(self.species.attackable([self.attacker, self.defender, self.neighborleft, self.neighborright]), True)

  def testPackHunting(self):
    self.attacker.setTraits([trait.Trait.pack_hunting])
    self.defender.setTraits([trait.Trait.herding])
    self.attacker.setPopulation(3)
    self.defender.setPopulation(5)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), True)

  def testFailPackHunting(self):
    self.attacker.setTraits([trait.Trait.pack_hunting])
    self.defender.setTraits([trait.Trait.herding])
    self.attacker.setPopulation(3)
    self.defender.setPopulation(6)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), False)

  def testBurrowing(self):
    self.defender.setTraits([trait.Trait.burrowing])
    self.defender.setFood(5)
    self.defender.setPopulation(5)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), False)

  def testFailBurrowing(self):
    self.defender.setTraits([trait.Trait.burrowing])
    self.defender.setFood(4)
    self.defender.setPopulation(5)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), True)

  def testHardShell(self):
    self.defender.setTraits([trait.Trait.hard_shell])
    self.attacker.setBodySize(5)
    self.defender.setBodySize(2)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), False)

  def testFailHardShell(self):
    self.defender.setTraits([trait.Trait.hard_shell])
    self.attacker.setBodySize(5)
    self.defender.setBodySize(1)
    self.assertEqual(self.species.attackable([self.attacker, self.defender, False, False]), True)

  def testAttackerAttacksSelf(self):
    with self.assertRaises(Exception("A species cannot attack itself")):
      self.species.attackable([self.attacker, self.attacker, False, False])

if __name__ == '__main__':
    unittest.main()