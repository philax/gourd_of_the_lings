import unittest
from controller.mob_gen import *

class TestMobGen(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestMobGen, self).__init__(*args, **kwargs)
		self.mob_gen = MobGen()