from mob import *
from mob_gen import *
from character import *

class Encounter(object):
	def __init__(self, character, seed=0): #seed for random numbers
		mob_maker = MobGen()
		self.mob = mob_maker.generate_mob()
		self.character = character
		print self.character

		print "A wild %s appeared!"% (self.mob.name)
		#self.battle()

	def mob_attack(self):
		self.character.lose_hp(5)

	def character_attack(self):
		self.mob.lose_hp(5)

	def battle(self):
		while self.character.is_alive() == True:
			while self.mob.is_alive() == True:
				# print "EVERYONE IS LIVING"
				self.character_attack()
				self.mob_attack()
			print "Victory!"
			return
			pass

	#  spawn mob
	#  //roll initiative?
	#  mob attack
	#  player attack
	#  repeat

	#
	# example random gen
	# Encounter (character, )
	# self.assertEquals(combat.random.randrange(0,100), 84)
	#

	#
	# fyi a tuple is an immutable array
	# check each exchange in combat, by building an array
	# resultes = [ x[0] for x in combat.history]
	#

	# exemplar / blueprint pattern
	#
	#