from mob import Mob

class MobGen(object):
	"""mob generator"""
	def __init__(self):
		# randomly generate mob stats here, eventually concat stats to a dict or array or some jazz
		pass

	def generate_mob(self, base_hp=10, name="Bergling", base_dmg=5, inventory=[]):
		mob = Mob(base_hp, name, base_dmg, inventory)
		return mob