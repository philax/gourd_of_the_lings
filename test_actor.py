import unittest
from actor import *

class TestActor(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestActor, self).__init__(*args, **kwargs)
		self.actor = Actor(100, "test actor", 10)

	def test_death(self):
		self.assertTrue(self.actor.is_alive())
		self.actor.hp = 0
		self.assertFalse(self.actor.is_alive())
		self.actor.hp = -1
		self.assertFalse(self.actor.is_alive())