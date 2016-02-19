import trait
import species

class Player:
  species_boards = []
  food_bag = 0
  hand = []
  player_id = 0

  def __init__(self, ident, loSpeciesBoard, bag):
    self.species_boards = loSpeciesBoard
    self.food_bag = bag
    self.hand = []
    self.player_id = ident

  def setSpeciesBoards(self, loSpeciesBoard):
    self.species_boards = loSpeciesBoard

  def getSpeciesBoards(self):
    return self.species_boards

  def setFoodBag(self, fb):
    self.food_bag = fb

  def getFoodBag(self):
    return self.food_bag

  def addToFoodBag(self, tokens):
    self.food_bag += tokens

  def setHand(self, cards):
    self.hand = cards

  def getHand(self):
    return self.hand

  def addToHand(self, cards):
    self.hand.extend(cards)

  def setPlayerId(self, ident):
    self.player_id = ident

  def getPlayerId(self):
    return self.player_id

  def feed(self, lop):
    # Holder for writing tests right now
    return true