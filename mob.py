from character import *
class Mob(Actor):
	def __init__(self, hp, name, inventory = []):
		print hp
		super(Mob, self).__init__(hp, name, inventory)
