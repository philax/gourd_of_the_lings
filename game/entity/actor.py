class Actor(object):
	def __init__(self, name, base_hp, base_dmg, inventory=[]):
		self.base_hp = base_hp
		self.hp = base_hp
		self.name = name
        # if(stats == None):
        #     self.stats['HP'] = 10
        #     self.stats['STR'] = 5
        #     self.stats['AGI'] = 5
        #     self.stats['DEX'] = 5


	def gain_hp(self, heal):
		self.hp += heal

	def lose_hp(self, dmg):
		self.hp -= dmg
		self.is_alive()

	def get_hp(self):
		print "%s has %s HP."% (self.name, self.hp)

	def is_alive(self, is_quiet=False):
		# print "DEBUG: Actor death check: %s has %s hp!"% (self.name, str(self.hp))
		if self.hp > 0:
			if is_quiet == False:
				self.get_hp()
			return True
		elif self.hp <= 0:
			if is_quiet == False: #hackey
				print "%s has been defeated!"% (self.name)
			return False