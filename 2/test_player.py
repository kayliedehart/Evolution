import unittest
import player
import collections

class TestPlayerMethods(unittest.TestCase):
  Card = collections.namedtuple('Card', ['face_value', 'bull_number'])
  card1 = Card(38, 2)
  card2 = Card(12, 7)
  card3 = Card(66, 5)
  card_impossible = Card(-2, 200)
  not_card = 50

  list_of_card = [card1, card2]
  default_player = player.Player(list_of_card)

  game1 = {'stacks': [list_of_card]}
  game2 = {}
  game3 = {'stacks':[]}
  game4 = {'stacks':[[card3, card3, card2], [card2, card1, card1], list_of_card ]}
  game5 = {'stacks':[list_of_card, [card3, card3, card2], [card2, card1, card_impossible]]}
  not_game = 250

  def test_init_(self):
    #when handed nothing
    self.assertEqual(player.Player([]).cards, [])
    #when handed a propper list of cards
    self.assertEqual(player.Player(self.list_of_card).cards, self.list_of_card)
    #when handed nonsense (aka not cards)
    (self.assertEqual(player.Player(['bread', 76, collections.defaultdict(int)]).cards,
                      ['bread', 76, collections.defaultdict(int)]))

  def test_receive_cards(self):
    #when handed more than one card
    (self.assertEqual(self.default_player.receive_cards([self.card3, self.card3]).cards,
                      [self.card1, self.card2, self.card3, self.card3]))
    #when handed one card
    (self.assertEqual(self.default_player.receive_cards(card3).cards,
                      [self.card1, self.card2, self.card3]))
    #when handed nonsense (aka not cards)
    (self.assertEqual(self.default_player.receive_cards('Thank you!').cards,
                      self.list_of_card.append('Thank you!')))

  def test_discard_card(self):
    #when handed a dictionary
    self.assertEqual(self.default_player.discard_card(self.game1), self.card1)
    #when handed a dictionary with no stacks
    self.default_player = player.Player(self.list_of_card)
    self.assertEqual(self.default_player.discard_card(self.game3), self.card1)
    #when handed nonsense
    self.default_player = player.Player(self.list_of_card)
    self.assertEqual(self.default_player.discard_card(self.not_game), self.card1)

  def test_get_stack_bull_value(self):
    #when handed no stack
    self.assertEqual(self.default_player.get_stack_bull_value([]), 0)
    #when handed a stack
    self.default_player = player.Player(self.list_of_card)
    self.assertEqual(self.default_player.get_stack_bull_value(self.list_of_card), 9)
    #when handed nonsense
    self.default_player = player.Player(self.list_of_card)
    self.assertEqual(self.default_player.get_stack_bull_value('cheese'), 0)

  def test_pick_stack(self):
    #when handed a game_state dictionary
    self.assertEqual(self.default_player.pick_stack(self.game4), 2)
    #when handed a dictionary with a stack that has an impossible bull point value
    self.assertEqual(self.default_player.pick_stack(self.game5), 0)
    with self.assertRaises(TypeError):
      self.default_player.pick_stack(self.game1)
      self.default_player.pick_stack(self.game2)
      self.default_player.pick_stack(self.game3)
      self.default_player.pick_stack(self.not_game)

if __name__ == '__main__':
    unittest.main()
