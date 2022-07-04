"""NPC Widget"""
import os
from configuration import BLOCK_SIZE, BLOCK_TIMES, WALK_SPEED
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.metrics import dp

class NPC(Image):
	"""Npc Widget"""
	from character.all_npc_move import random_npc_movement
	def __init__(self, position=(0,0), sprite="", move="", npc_id=0, script="", **kwargs):
		super().__init__(**kwargs)
		self.all_variable()
		self.allow_stretch = True
		self.anim_loop = 1
		self.movement = move
		self.source = sprite
		self.npc_id = npc_id
		self.script = script
		self.npc_frame()
		self.size = (self.block_size, dp((BLOCK_SIZE*2)*BLOCK_TIMES))
		self.position = (position)
		if os.path.exists(sprite): self.texture.mag_filter = "nearest"
		Clock.schedule_once(lambda _: self.update_location(), 0)
		self.bind(texture = self.change_texture)
		self.check_npc_movement()
	
	def check_npc_movement(self):
		"""Check Npc Movement"""
		if self.movement == "random":
			self.move_npc_clock = Clock.create_trigger(lambda _: self.random_npc_movement(), 3)
			self.move_npc_clock()
		else:
			self.move_npc_clock = Clock.create_trigger(lambda _: None)
	
	def all_variable(self):
		"""All Variable"""
		self.range = 1
		self.mover_x = 0
		self.mover_y = 0
		self.npc_look = "down"
		self.up_look = "left"
		self.down_look = "left"
		self.left_look = "left"
		self.right_look = "left"
		self.look_up_left = ""
		self.look_up_right = ""
		self.look_down_left = ""
		self.look_down_right = ""
		self.look_left_left = ""
		self.look_left_right = ""
		self.look_right_left = ""
		self.look_right_right = ""
		self.block_size = dp(BLOCK_SIZE*BLOCK_TIMES)

	def change_texture(self, widget, _):
		"""Change Texture"""
		if os.path.exists(self.source):
			widget.texture.mag_filter = "nearest"
	
	def update_location(self):
		"""Update Location"""
		self.parent.parent.npc_position(self, *self.position)
		self.permanent_position = self.position

	def npc_frame(self):
		"""Npc Frame"""
		if (self.source == "assets/character/npc1/down.png"
		or self.source == "assets/character/npc1/left.png"
		or self.source == "assets/character/npc1/up.png"
		or self.source == "assets/character/npc1/right.png"):
			self.look_up_left = "assets/character/npc1/look_up_left.zip"
			self.look_up_right = "assets/character/npc1/look_up_right.zip"
			self.look_down_left = "assets/character/npc1/look_down_left.zip"
			self.look_down_right = "assets/character/npc1/look_down_right.zip"
			self.look_left_left = "assets/character/npc1/look_left_left.zip"
			self.look_left_right = "assets/character/npc1/look_left_right.zip"
			self.look_right_left = "assets/character/npc1/look_right_left.zip"
			self.look_right_right = "assets/character/npc1/look_right_right.zip"

	def move_up(self):
		"""Move Up"""
		self.anim_delay = 0.1
		if self.up_look == "left":
			self.source = self.look_up_right
			self.up_look = "right"
		else:
			self.source = self.look_up_left
			self.up_look = "left"
		self.anim_delay = WALK_SPEED
		self.npc_look = "up"
	
	def move_down(self):
		"""Move Down"""
		self.anim_delay = 0.1
		if self.down_look == "left":
			self.source = self.look_down_right
			self.down_look = "right"
		else:
			self.source = self.look_down_left
			self.down_look = "left"
		self.anim_delay = WALK_SPEED
		self.npc_look = "down"

	def move_left(self):
		"""Move Down"""
		self.anim_delay = 0.1
		if self.left_look == "left":
			self.source = self.look_left_right
			self.left_look = "right"
		else:
			self.source = self.look_left_left
			self.left_look = "left"
		self.anim_delay = WALK_SPEED
		self.npc_look = "left"

	def move_right(self):
		"""Move Down"""
		self.anim_delay = 0.1
		if self.right_look == "left":
			self.source = self.look_right_right
			self.right_look = "right"
		else:
			self.source = self.look_right_left
			self.right_look = "left"
		self.anim_delay = WALK_SPEED
		self.npc_look = "right"

	def npc_script(self):
		"""Npc Script"""
		self.parent.parent.message_box()
		if self.script == "":
			self.parent.parent.remove_message_box()
			self.move_npc_clock()

	def move_npc_right(self):
		"""Move Npc"""
		if self.mover_x == 0:
			self.move_right()
			self.parent.parent.all_npc_position[self.parent.
			parent.all_npc_list.index(self)] = self.get_position("r")
		self.x += self.block_size/20
		self.mover_x += self.block_size/20
		if self.mover_x >= self.block_size:
			self.position = self.get_position("z")
			self.move_npc_clock()
			return False
	
	def move_npc_left(self):
		"""Move Npc"""
		if self.mover_x == 0:
			self.move_left()
			self.parent.parent.all_npc_position[self.parent.
			parent.all_npc_list.index(self)] = self.get_position("l")
		self.x -= self.block_size/20
		self.mover_x -= self.block_size/20
		if abs(self.mover_x) >= self.block_size:
			self.position = self.get_position("z")
			self.move_npc_clock()
			return False

	def move_npc_up(self):
		"""Move Npc"""
		if self.mover_y == 0:
			self.move_up()
			self.parent.parent.all_npc_position[self.parent.
			parent.all_npc_list.index(self)] = self.get_position("u")
		self.y += self.block_size/20
		self.mover_y += self.block_size/20
		if self.mover_y >= self.block_size:
			self.position = self.get_position("z")
			self.move_npc_clock()
			return False

	def move_npc_down(self):
		"""Move Npc"""
		if self.mover_y == 0:
			self.move_down()
			self.parent.parent.all_npc_position[self.parent.
			parent.all_npc_list.index(self)] = self.get_position("d")
		self.y -= self.block_size/20
		self.mover_y -= self.block_size/20
		if abs(self.mover_y) >= self.block_size:
			self.position = self.get_position("z")
			self.move_npc_clock()
			return False
	
	def get_position(self, m=""):
		"""Get Position"""
		(r_pos, c_pos) = self.parent.parent.all_npc_position[
			self.parent.parent.all_npc_list.index(self)]
		if m == "d": r_pos+=1
		elif m == "u": r_pos-=1
		elif m == "l": c_pos-=1
		elif m == "r": c_pos+=1
		elif m == "z": self.mover_x, self.mover_y = (0,0)
		return (r_pos, c_pos)

	def restriction(self, m=""):
		"""Restriction"""
		if m!="u" and m!="d" and m!="l" and m!="r": return False
		row, col = self.get_position(m)
		position = self.parent.parent.pos_row, self.parent.parent.pos_col
		if (row, col) == (position): return True
		elif m=="u":
			if ((row-1, col) == (position)
			 or (row, col+1) == (position)
			 or (row, col-1) == (position)):
				return True
		elif m=="d":
			if ((row+1, col) == (position)
			 or (row, col+1) == (position)
			 or (row, col-1) == (position)):
				return True
		elif m=="l":
			if ((row+1, col) == (position)
			 or (row-1, col) == (position)
			 or (row, col-1) == (position)):
				return True
		elif m=="r":
			if ((row+1, col) == (position)
			 or (row-1, col) == (position)
			 or (row, col+1) == (position)):
				return True
		if self.parent.parent.current_world.world_behavior[row][col] != 0:
			return True
		return False
