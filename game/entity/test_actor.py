import unittest
from game.entity.actor import *

class TestActor(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestActor, self).__init__(*args, **kwargs)
		self.actor = Actor("test actor", 100, 10)

	def test_death(self):
		self.assertTrue(self.actor.is_alive())
		self.actor.hp = 0
		self.assertFalse(self.actor.is_alive())
		self.actor.hp = -1
		self.assertFalse(self.actor.is_alive())