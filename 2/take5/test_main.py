# Unit-testing suite for 6 Nimmt! methods in main component

import unittest
import dealer
import components
import player
import main

class TestMainMethods(unittest.TestCase):

  def setUp(self):
    self.game = main(4)

  def tearDown(self):
    del self.game

  def test_end_of_round(self):
      # a game that's over
      # a game that needs another round

if __name__ == '__main__':
    unittest.main()