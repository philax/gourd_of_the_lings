from actor import *
class Character(Actor):
	def __init__(self, base_hp, name, base_dmg, inventory=[]):
		super(Character, self).__init__(base_hp, name, base_dmg)
		self.xp = 0

	def is_alive(self, is_quiet=False):
		# print "DEBUG: Character death check for hp: %s"% (self.hp)
		if self.hp > 0:
			if is_quiet == False:
				self.get_hp()
			return True
		elif self.hp <= 0:
			print "%s has fallen in battle!"% (self.name)
			return False

	#
	# example of modding hp off of player experience
	# + int(20*math.log(self._exp,10))