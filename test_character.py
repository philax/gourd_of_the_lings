import unittest
from character import *

class TestCharacter(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestCharacter, self).__init__(*args, **kwargs)
		self.character = Character(100, "test dude", 10)

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