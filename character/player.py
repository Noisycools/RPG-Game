"""Player Widget"""
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.metrics import dp

from configuration import BLOCK_SIZE, BLOCK_TIMES
class Player(Image):
	"""Player Widget"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.allow_stretch = True
		self.anim_loop = 1
		self.size = (dp((BLOCK_SIZE)*BLOCK_TIMES), dp((BLOCK_SIZE*2)*BLOCK_TIMES))
		self.x = (Window.width//2)-dp(25)
		self.y = (Window.height//2)-dp(25)
		self.source = "assets/character/player/down.png"
		self.bind(texture = self.change_texture)
		self.texture.mag_filter = "nearest"
	
	def change_texture(self, widget, _):
		"""Change Texture"""
		widget.texture.mag_filter = "nearest"

class PlayerHead(Image):
	"""Player Head"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.allow_stretch = True
		self.anim_loop = 1
		self.size = (dp((BLOCK_SIZE)*BLOCK_TIMES), dp((BLOCK_SIZE)*BLOCK_TIMES))
		self.x = (Window.width//2)-dp(25)
		self.source = "assets/character/playerhead/down.png"
		self.bind(texture = self.change_texture)
		self.texture.mag_filter = "nearest"
	
	def change_texture(self, widget, _):
		"""Change Texture"""
		widget.texture.mag_filter = "nearest"
