"""Right"""
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.animation import Animation
from configuration import CONTROLLER_SIZE, WALK_SPEED, RUN_SPEED

class RightButton(Image):
	"""Right Button"""
	def __init__(self, **kw):
		super().__init__(**kw)
		self.allow_stretch = True
		self.moving = False
		self.player_pic = "left"
		self.size = (dp(CONTROLLER_SIZE), dp(CONTROLLER_SIZE))
		self.pos = (dp(CONTROLLER_SIZE*2), 0)
		self.source = "assets/controller/RIGHT.png"

	def on_touch_down(self, touch):
		"""On Touch Down"""
		if self.collide_point(*touch.pos):
			self.parent.touched = False
			if self.parent.walk_left or self.moving: return False
			elif self.parent.down_button.moving:
				self.parent.down_button.anim.on_complete = lambda _: self.cancel_walk_1(touch)
			elif self.parent.up_button.moving:
				self.parent.up_button.anim.on_complete = lambda _: self.cancel_walk_2(touch)
			elif (self.parent.look_position != "right"
			and self.condition()): self.look_only(touch)
			else: self.timer = Clock.schedule_once(lambda _: self.activate_walk(touch), 0.1)

	def cancel_walk_1(self, touch):
		"""Cancel Walking Animation"""
		self.parent.touched = False
		touch.ungrab(self.parent.down_button)
		self.parent.down_button.complete()
		self.parent.player.anim_delay = 0.1
		self.parent.player_head.anim_delay = self.parent.player.anim_delay
		self.animate_walk()
		self.timer = Clock.schedule_once(lambda _: self.activate_walk(touch), 0.1)

	def cancel_walk_2(self, touch):
		"""Cancel Walking Animation"""
		self.parent.touched = False
		touch.ungrab(self.parent.up_button)
		self.parent.up_button.complete()
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
			self.parent.look_position = "right"
			self.parent.player.source = "assets/character/player/look_right_right.zip"
			self.player_pic = "right"
		else:
			self.parent.look_position = "right"
			self.parent.player.source = "assets/character/player/look_right_left.zip"
			self.player_pic = "left"
		self.parent.player_head.source = "assets/character/playerhead/right.png"
		self.parent.player_head.source = "assets/character/playerhead/right_walk.zip"

	def activate_walk(self, touch):
		"""Activate Walk"""
		touch.grab(self)
		self.moving = True
		self.parent.walk_right = True
		self.parent.touched = True
		self.walk_animation(touch)

	def on_touch_up(self, touch):
		"""On Touch Up"""
		try: self.timer.cancel()
		except AttributeError: pass
		if touch.grab_current is self:
			touch.ungrab(self)
			self.anim.on_complete = lambda _: self.complete()

	def complete(self):
		"""Execute After Completing Walk"""
		self.moving = False
		self.parent.walk_right = False
	
	def cancel_walk_3(self, touch):
		"""Cancel Walking Main"""
		touch.ungrab(self)
		self.complete()
	
	def condition(self):
		"""Condition"""
		if (self.parent.up_button.moving is False
		and self.parent.left_button.moving is False
		and self.parent.down_button.moving is False):
			return True
		else: return False

	def check_restriction(self):
		"""Check Restriction"""
		try:
			if self.parent.current_world.world_behavior[self.parent.pos_row][self.parent.pos_col+1] == 0:
				if (self.parent.pos_row, self.parent.pos_col+1) in self.parent.all_npc_position:
					return True
				return False
			elif self.parent.current_world.world_behavior[self.parent.pos_row][self.parent.pos_col+1] == 1:
				return True
		except IndexError: return True

	def walk_animation(self, touch):
		"""Walk Animation"""
		if self.condition() is False or self.check_restriction(): self.cancel_walk_3(touch)
		if self.parent.touched is False: self.cancel_walk_3(touch)
		if self.moving is False or self.parent.left_button.moving: return False
		self.parent.player.anim_delay = WALK_SPEED if self.parent.running is False else RUN_SPEED
		self.parent.player_head.anim_delay = self.parent.player.anim_delay
		self.anim = Animation(x = self.parent.current_world.x-self.parent.block_size,
			d=(WALK_SPEED*2 if self.parent.running is False else RUN_SPEED*2), t="linear")
		self.parent.pos_col += 1
		self.anim.start(self.parent.current_world)
		self.parent.update_coordinate()
		self.animate_walk()
		self.anim.on_complete = lambda _: self.walk_animation(touch)
