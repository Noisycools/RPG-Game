"""Message"""
from kivy.uix.image import Image
from kivy.core.window import Window
#from configuration import BLOCK_SIZE, BLOCK_TIMES
from kivy.metrics import dp

class MessageBox(Image):
	"""Message Box"""
	def __init__(self, **kw):
		super().__init__(**kw)
		self.source = "assets/message_box.png"
		self.allow_stretch = True
		self.keep_ratio = False
		if Window.width < Window.height:
			self.size = (Window.width-dp(20), dp(100))
		else: self.size = (Window.width-dp(20), dp(100))
		self.pos = (dp(10), dp(10))
		self.texture.mag_filter = "nearest"