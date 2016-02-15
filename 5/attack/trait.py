# Trait cards for a Species in the game Evolution

from enum import Enum

class Trait(Enum):

	def isAid(self):
		"""
		Checks whether the given Trait is Aid: that is, if it helps
		neighboring Species.
		"""
		return False

	def isOffensive(self):
		"""
		Checks whether the given Trait is Offensive
		"""
		return False

	def isDefensive(self):
		"""
		Checks whether the given Trait is Defensive
		"""
		return False

	def isNeutral(self):
		"""
		Checks whether the given Trait is Neutral
		"""
		return False

class Aid(Trait):
	warning_call = "warning-call"
	symbiosis = "symbiosis"

	def isAid(self):
		"""
		Checks whether the given Trait is Aid: that is, if it helps
		neighboring Species.
		"""
		return True

class Offensive(Trait):
	carnivore = "carnivore"
	ambush = "ambush"
	climbing = "climbing"
	pack_hunting = "pack-hunting"

	def isOffensive(self):
		"""
		Checks whether the given Trait is Offensive
		"""
		return True

class Defensive(Trait):
	burrowing = "burrowing"
	hard_shell = "hard-shell"
	herding = "herding"

	def isDefensive(self):
		"""
		Checks whether the given Trait is Defensive
		"""
		return True

class Neutral(Trait):
	cooperation = "cooperation"
	horns = "horns"
	fat_tissue = "fat-tissue"
	fertile = "fertile"
	foraging = "foraging"
	long_neck = "long-neck"
	scavenger = "scavenger"

	def isNeutral(self):
		"""
		Checks whether the given Trait is Neutral
		"""
		return True

