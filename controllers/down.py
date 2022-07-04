"""Down"""
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.animation import Animation
from configuration import CONTROLLER_SIZE, WALK_SPEED, RUN_SPEED

class DownButton(Image):
	"""Down Button"""
	def __init__(self, **kw):
		super().__init__(**kw)
		self.allow_stretch = True
		self.moving = False
		self.player_pic = "left"
		self.size = (dp(CONTROLLER_SIZE), dp(CONTROLLER_SIZE))
		self.pos = (dp(CONTROLLER_SIZE), 0)
		self.source = "assets/controller/DOWN.png"

	def on_touch_down(self, touch):
		"""On Touch Down"""
		if self.collide_point(*touch.pos):
			self.parent.touched = False
			if self.parent.walk_up or self.moving: return False
			elif self.parent.left_button.moving:
				self.parent.left_button.anim.on_complete = lambda _: self.cancel_walk_1(touch)
			elif self.parent.right_button.moving:
				self.parent.right_button.anim.on_complete = lambda _: self.cancel_walk_2(touch)
			elif (self.parent.look_position != "down"
			and self.condition()): self.look_only(touch)
			else: self.timer = Clock.schedule_once(lambda _: self.activate_walk(touch), 0.1)

	def cancel_walk_1(self, touch):
		self.parent.touched = False
		touch.ungrab(self.parent.left_button)
		self.parent.left_button.complete()
		self.parent.player.anim_delay = 0.1
		self.parent.player_head.anim_delay = self.parent.player.anim_delay
		self.animate_walk()
		self.timer = Clock.schedule_once(lambda _: self.activate_walk(touch), 0.1)
	
	def cancel_walk_2(self, touch):
		self.parent.touched = False
		touch.ungrab(self.parent.right_button)
		self.parent.right_button.complete()
		self.parent.player.anim_delay = 0.1
		self.parent.player_head.anim_delay = self.parent.player.anim_delay
		self.animate_walk()
		self.timer = Clock.schedule_once(lambda _: self.activate_walk(touch), 0.1)

	def look_only(self, touch):
		"""Look Only"""
		self.parent.player.anim_delay = 0.1
		self.parent.player_head.anim_delay = self.parent.player.anim_delay
		self.animate_walk()
		self.timer = Clock.schedule_once(lambda _: self.activate_walk(touch), 0.1)

	def animate_walk(self):
		"""Animate Walk"""
		if self.player_pic == "left":
			self.parent.look_position = "down"
			self.parent.player.source = "assets/character/player/look_down_right.zip"
			self.player_pic = "right"
		else:
			self.parent.look_position = "down"
			self.parent.player.source = "assets/character/player/look_down_left.zip"
			self.player_pic = "left"
		self.parent.player_head.source = "assets/character/playerhead/down.png"
		self.parent.player_head.source = "assets/character/playerhead/down_walk.zip"
		#self.parent.player_head.reload()

	def activate_walk(self, touch):
		"""Activate Walk"""
		touch.grab(self)
		self.moving = True
		self.parent.touched = True
		self.parent.walk_down = True
		self.walk_animation(touch)
	
	def on_touch_up(self, touch):
		"""On Touch Up"""
		try: self.timer.cancel()
		except AttributeError: pass
		if touch.grab_current is self:
			touch.ungrab(self)
			self.anim.on_complete = lambda _: self.complete()

	def complete(self):
		self.moving = False
		self.parent.walk_down = False
	
	def cancel_walk_3(self, touch):
		touch.ungrab(self)
		self.complete()
	
	def condition(self):
		"""Condition"""
		if (self.parent.up_button.moving is False
		and self.parent.left_button.moving is False
		and self.parent.right_button.moving is False):
			return True
		else: return False
	
	def check_restriction(self):
		"""Check Restriction"""
		try:
			if self.parent.current_world.world_behavior[self.parent.pos_row+1][self.parent.pos_col] == 0:
				if (self.parent.pos_row+1, self.parent.pos_col) in self.parent.all_npc_position:
					return True
				return False
			elif self.parent.current_world.world_behavior[self.parent.pos_row+1][self.parent.pos_col] == 1:
				return True
		except IndexError: return True

	def walk_animation(self, touch):
		"""Walk Animation"""
		if self.condition() is False or self.check_restriction(): self.cancel_walk_3(touch)
		if self.parent.touched is False: self.cancel_walk_3(touch)
		if self.moving is False or self.parent.up_button.moving: return False
		self.parent.player.anim_delay = WALK_SPEED if self.parent.running is False else RUN_SPEED
		self.parent.player_head.anim_delay = self.parent.player.anim_delay
		self.anim = Animation(y = self.parent.current_world.y+self.parent.block_size,
			d=(WALK_SPEED*2 if self.parent.running is False else RUN_SPEED*2), t="linear")
		self.parent.pos_row += 1
		self.anim.start(self.parent.current_world)
		self.parent.update_coordinate()
		self.animate_walk()
		self.anim.on_complete = lambda _: self.walk_animation(touch)
