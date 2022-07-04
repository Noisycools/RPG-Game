"""A"""
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.metrics import dp
#from kivy.clock import Clock
from kivy.core.window import Window
#from kivy.animation import Animation
from configuration import CONTROLLER_SIZE

class AButton(ButtonBehavior, Image):
	"""A Button"""
	def __init__(self, **kw):
		super().__init__(**kw)
		self.allow_stretch = True
		self.size = (dp(CONTROLLER_SIZE), dp(CONTROLLER_SIZE))
		self.pos = (Window.width-dp(CONTROLLER_SIZE), 0)
		self.source = "assets/controller/A.png"
	
	def on_release(self):
		"""On Release"""
		if self.parent.look_position == "down":
			position = (self.parent.pos_row+1, self.parent.pos_col)
			if position in self.parent.all_npc_position:
				widget = self.parent.all_npc_list[self.parent.all_npc_position.index(position)]
				if widget.npc_look != "up":
					widget.move_up()
					widget.npc_look = "up"
				widget.move_npc_clock.cancel()
				widget.npc_script()
		elif self.parent.look_position == "left":
			position = (self.parent.pos_row, self.parent.pos_col-1)
			if position in self.parent.all_npc_position:
				widget = self.parent.all_npc_list[self.parent.all_npc_position.index(position)]
				if widget.npc_look != "right":
					widget.move_right()
					widget.npc_look = "right"
				widget.move_npc_clock.cancel()
				widget.npc_script()
		elif self.parent.look_position == "up":
			position = (self.parent.pos_row-1, self.parent.pos_col)
			if position in self.parent.all_npc_position:
				widget = self.parent.all_npc_list[self.parent.all_npc_position.index(position)]
				if widget.npc_look != "down":
					widget.move_down()
					widget.npc_look = "down"
				widget.move_npc_clock.cancel()
				widget.npc_script()
		elif self.parent.look_position == "right":
			position = (self.parent.pos_row, self.parent.pos_col+1)
			if position in self.parent.all_npc_position:
				widget = self.parent.all_npc_list[self.parent.all_npc_position.index(position)]
				if widget.npc_look != "left":
					widget.move_left()
					widget.npc_look = "left"
				widget.move_npc_clock.cancel()
				widget.npc_script()

