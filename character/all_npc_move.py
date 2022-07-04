"""All Move"""
import random
from kivy.clock import Clock

def random_npc_movement(self):
	"""Npc Movement"""
	rand = random.choice([
		"ll", "lr", "ld", "lu",
		"r", "l", "u", "d",
		"r", "l", "u", "d",])
	if self.restriction(rand): self.move_npc_clock()
	elif rand == "r":
		if self.permanent_position[1]+self.range<=self.position[1]:
			self.move_npc_clock()
		else: Clock.schedule_interval(lambda _:self.move_npc_right(), 1/60)
	elif rand == "l":
		if self.permanent_position[1]-self.range>=self.position[1]:
			 self.move_npc_clock()
		else: Clock.schedule_interval(lambda _:self.move_npc_left(), 1/60)
	elif rand == "u":
		if self.permanent_position[0]-self.range>=self.position[0]:
			self.move_npc_clock()
		else: Clock.schedule_interval(lambda _:self.move_npc_up(), 1/60)
	elif rand == "d":
		if self.permanent_position[0]+self.range<=self.position[0]:
			self.move_npc_clock()
		else: Clock.schedule_interval(lambda _:self.move_npc_down(), 1/60)
	elif rand == "lr":
		if self.npc_look != "right": self.move_right()
		self.move_npc_clock()
	elif rand == "ll":
		if self.npc_look != "left": self.move_left()
		self.move_npc_clock()
	elif rand == "ld":
		if self.npc_look != "down": self.move_down()
		self.move_npc_clock()
	elif rand == "lu":
		if self.npc_look != "up": self.move_up()
		self.move_npc_clock()
