from actor import *
class Character(Actor):
	def __init__(self, hp, name):
		super(Character, self).__init__(hp, name)

	def is_alive(self):
		print "DEBUG: Character death check for hp: %s"% (self.hp)
		if self.hp > 0:
			return True
		elif self.hp <= 0:
			# GAME OVER MAN
			return False

	#
	# example of modding hp off of player experience
	# + int(20*math.log(self._exp,10))