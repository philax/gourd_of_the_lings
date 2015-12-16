class Actor(object):
	def __init__(self, hp, name, inventory=[]):
		self.hp = hp
		self.name = name
		self.xp = 0

	def gain_hp(self, heal):
		self.hp += heal

	def lose_hp(self, dmg):
		self.hp -= dmg
		self.is_alive()
		pass

	def gain_xp(self, gain):
		self.xp += gain

	def is_alive(self):
		print "DEBUG: Actor death check: %s has %s hp!"% (self.name, str(self.hp))
		if self.hp > 0:
			return True
		elif self.hp <= 0:
			return False