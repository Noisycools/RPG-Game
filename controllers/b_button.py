"""B"""
from kivy.uix.image import Image
from kivy.metrics import dp
#from kivy.clock import Clock
from kivy.core.window import Window
#from kivy.animation import Animation
from configuration import CONTROLLER_SIZE

class BButton(Image):
	"""B Button"""
	def __init__(self, **kw):
		super().__init__(**kw)
		self.allow_stretch = True
		self.size = (dp(CONTROLLER_SIZE), dp(CONTROLLER_SIZE))
		self.pos = (Window.width-dp(CONTROLLER_SIZE*2), 0)
		self.source = "assets/controller/B.png"
	
	def on_touch_down(self, touch):
		"""On Touch Down"""
		if self.collide_point(*touch.pos):
			self.parent.running = True
			touch.grab(self)
	
	def on_touch_up(self, touch):
		"""On Touch Up"""
		if touch.grab_current is self:
			self.parent.running = False
			touch.ungrab(self)
