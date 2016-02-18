import trait
import species

class Player:
  species_boards = []
  food_bag = 0
  hand = []

  def __init__(self):
    species_boards = []
    food_bag = 0
    hand = []

  def setSpeciesBoards(self, loSpeciesBoard):
    species_boards = loSpeciesBoard

  def getSpeciesBoards(self):
    return species_boards

  def setFoodBag(self, fb):
    food_bag = fb

  def getFoodBag(self):
    return food_bag

  def addToFoodBag(self, tokens):
    food_bag = food_bag + tokens

  def setHand(self, cards):
    hand = cards

  def getHand(self):
    return hand

  def addToHand(self, cards):
    hand.extend(cards)

  def feed(self, lop):
    # Holder for writing tests right now
    return true