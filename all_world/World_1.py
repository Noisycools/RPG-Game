"""Field 1.0"""
from behavior.b1_0 import Behavior
from configuration import BLOCK_SIZE, BLOCK_TIMES
from kivy.uix.image import Image
from kivy.metrics import dp

class World1_0(Image):
	"""1.1 World"""
	def __init__(self, **kw):
		super().__init__(**kw)
		self.allow_stretch = True
		self.block_size = dp(BLOCK_SIZE*BLOCK_TIMES)
		self.world_behavior = Behavior
		self.world_size = (len(Behavior), len(Behavior[0]))
		self.size = (self.block_size*self.world_size[0],
			self.block_size*self.world_size[1])
		self.source = "assets/world/1_0.png"
		self.texture.mag_filter = "nearest"
