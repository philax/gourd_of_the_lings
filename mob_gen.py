from mob import Mob

class MobGen(object):
	"""mob generator"""
	def __init__(self):
		# randomly generate mob stats here, eventually concat stats to a dict or array or some jazz
		pass

	def generate_mob(self, hp = 10, name = "Bergling", inventory = []):
		mob = Mob(hp, name, inventory)
		return mob