from entity.mob import Mob

class MobGen(object):
	"""mob generator"""
	def __init__(self):
		# randomly generate mob stats here, eventually concat stats to a dict or array or some jazz
		pass

	def generate_mob(self, name="Bergling", base_hp=10, base_dmg=5, inventory=[]):
		mob = Mob(name, base_hp, base_dmg, inventory)
		return mob