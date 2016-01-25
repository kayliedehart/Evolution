import unittest
import components

class TestCardMethods(unittest.TestCase):
  def setUp(self):
    self.card1 = card.Card(1, 1)
    self.card2 = card.Card(2, 2)

  def tearDown(self):
    del self.card

  def testGetNumber(self):
    self.assertEqual(self.card1.getNumber == 1)

  def testSetNumber(self):
    self.card1.setNumber(2)
    self.assertEqual(self.card1 == card.Card(2, 1))

  def testGetBullNumber(self):
    self.assertEqual(self.card1.getBullNumber == 1)

  def testSetBullNumber(self):
    self.card2.setBullNumber(3)
    self.assertEqual(card2 == card.Card(2, 3))


if __name__ == '__main__':
  unittest.main()