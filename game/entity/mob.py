from character import *
class Mob(Actor):
	def __init__(self, name, base_hp, base_dmg, inventory = []):
		super(Mob, self).__init__(name, base_hp, base_dmg, inventory)
