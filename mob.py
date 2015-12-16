from character import *
class Mob(Actor):
	def __init__(self, base_hp, name, base_dmg, inventory = []):
		super(Mob, self).__init__(base_hp, name, base_dmg, inventory)
