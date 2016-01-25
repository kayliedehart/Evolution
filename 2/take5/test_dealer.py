# Unit-testing suite for 6 Nimmt! methods in dealer component

import unittest
import dealer
import components
import player

class TestDealerMethods(unittest.TestCase):

  def setUp(self):
    self.dealer = dealer.Dealer()

  def tearDown(self):
    del self.dealer

  def testDealFirst(self):
    # a game with no players
    # a game with players

  def testMakeStacks(self):
    # just create four stacks

  def testUpdateStacks(self):
    # player's card just added to stack
    # player's card overflows, give them the current, reset stack with their card
    # give player choice of stacks

if __name__ == '__main__':
    unittest.main()