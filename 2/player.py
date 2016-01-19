# Implements a Player in a game of 6 Nimmt! according to provided interface

class Player:
  cards = []

  def _init_(self,cards):
    self.cards=cards

  def receive_cards(self,cards):
    for card in cards:
      self.cards.append(card)

  def discard_card(self, game_state):
    chosen = cards[0]
    for card in self.cards:
      if(chosen.face_value<card.face_value):
        chosen=card

    self.cards.remove(chosen)
    return chosen

  def get_stack_bull_value(stack):
    stack_value = 0

    for card in stack:
      stack_value += card.bull_number

    return stack_value

  def pick_stack(self, game_state):
    smallest_stack = game_state["stacks"][0]
    smallest_value = self.get_stack_bull_value(game_state["stacks"][0])

    for stack in game_state["stacks"][1:]:
        stack_value = self.get_stack_bull_value(stack)

        if(stack_value<smallest_value):
          smallest_value = stack_value
          smallest_stack = stack

    return game_state["stacks"].indexOf(smallest_stack)

