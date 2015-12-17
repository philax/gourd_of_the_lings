from entity.mob import *
from controller.mob_gen import *
from entity.character import *

class Encounter(object):
	def __init__(self, character, seed=0): #seed for random numbers
		mob_maker = MobGen()
		self.mob = mob_maker.generate_mob()
		self.character = character
		self.dmg = 0

		print "A wild %s appeared!"% (self.mob.name)
		#self.battle()

	def mob_attack(self):
		self.dmg = 5
		print "%s attacks %s for %s damage!"% (self.mob.name, self.character.name, self.dmg)
		self.character.lose_hp(self.dmg)

	def character_attack(self):
		self.dmg = 5
		print "%s attacks %s for %s damage!"% (self.character.name, self.mob.name, self.dmg)
		self.mob.lose_hp(self.dmg)

	#
	# todo: split battle to rounds and turns
	#
	def battle(self):
		while self.character.is_alive(True) == True:
			while self.mob.is_alive(True) == True:
				# print "EVERYONE IS LIVING"
				self.character_attack()
				if self.mob.is_alive(True) == True:
					self.mob_attack()
			print "Victory!"
			return
			print "Uh oh!"

	#  spawn mob
	#  prompt to attack? or flee?
	#  attack
	#  check if mob is a live
	#
	#
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