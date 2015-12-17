import unittest
from entitity.character import *

class TestCharacter(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestCharacter, self).__init__(*args, **kwargs)
		self.character = Character("test dude", 100, 10)
		print sys.path

	def test_death(self):
		self.assertTrue(self.character.is_alive())
		self.character.hp = 0
		self.assertFalse(self.character.is_alive())
		self.character.hp = -1
		self.assertFalse(self.character.is_alive())

	def test_xpgain(self):
		self.assertEqual(self.character.xp, 0)
		self.character.gain_xp(10)
		self.assertEquals(self.character.xp, 10)