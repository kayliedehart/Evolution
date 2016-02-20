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

  def canFeed(self):
  """
  Checks if the call to feed follows the sequencing constraints
  throws an error if it doesn't match specs
  """
    #checks if there are not enough species boards
    if ((self.species_boards.size() != 0)
      or (not ((self.species_boards.size() == 1)
        and (self.species_boards[0].isCarnivore())))):

      #checks if there are an appropraite number of hungry animals
      numHungry = 0
      for animal in self.species_boards:
        if animal.getPopulation() > animal.getFood():
          numHungery = numHungery + 1

      if notHungery = 1:
        Exception("Violation of Sequencing Constraints")
      if notHungery = 0:
        return False
      else:
        return True
    else:
      Exception("Violation of Sequencing Constraints")

  def sortByFat(self, loa):
    if (loa.size() > 1):
      return sorted(self.species_boards, key=lambda species: species.bodysize, reverse = True)
    else:
      return loa

  def feedNext(self):
  """
  Determines the next species that needs to be fed
  """
  fat_species = []
  carnivores = []
  herbavores = []

  sortedByFatSpeciesBoards = self.sortByFat(self.species_boards)

  #catagorizes all of the species this player has
  for animal in sortedByFatSpeciesBoards:
    if (animal.getFood() < animal.getPopulation()):
      if (animal.hasFatTissue()):
        fat_species.append(animal)
      elif (animal.isCarnivore())
        carnivores.append(animal)
      else:
        herbavores.append(animal)

  #returns the fattest of the prioritized species
  if fat_species:
    return (fat_species[0], Trait.fat_species)
  elif herbavores:
    return (herbavores[0], False)
  elif carnivores:
    return (carnivores[0], Trait.carnivores)
  else:
    Exception("Violation of Sequencing Constraints")

  def compileSpecies(self, lop):
    """
    Compiles all the species boards from the list of players provided
    """
    boards = []
    for player in lop:
      boards.extend(player.getSpeciesBoards)
    return boards

  def pickVictim(self, carni, lop):
    """
    picks a victim for the given carnivore from the list of players' species
    """
    #compile lists of all species
    boards = self.compileSpecies(lop)
    #sort it in order of size.
    boards = sorted(boards, key=lambda species: species.bodysize, reverse = True)
    #go down the list until it finds something it can eat
    for board in boards:
      situation = [carni, board, ]
      if board.attackable(situation):
        return board

    #if it cant eat anything return false
    return False

  def feed(self, lop):
    """
    Determines which species the player is going to feed
    """
    if(not self.canFeed()):
      return False
    chosen, trait = self.feedNext()

    if (not trait):
      return chosen
    elif (isinstance(Trait.carnivore, trait)):
      victim = self.pickVictim(chosen, lop)
      if (not victim):
        return False
      else:
        return chosen, victim
    else:
      return chosen, (chosen.getPopulation - chosen.getFood)