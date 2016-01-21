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

  def test_deal_first(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_make_stacks(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())
  def test_se_tstacks(self):
      self.assertTrue()
  def test_update_stacks(self):
      self.assertTrue()
      self.assertFalse()


if __name__ == '__main__':
    unittest.main()