"""RPG make"""
import sys
from kivy.app import App, runTouchApp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import sp, dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from src import InterfaceWidget

class RPGGameApp(App):
	"""RPG Remake"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		Window.size = (round(Window.width), round(Window.height))
		Window.bind(on_keyboard = self.keyboard)

	def keyboard(self, _, key, *__):
		"""On Keyboard"""
		if key == 27: return True

	def build(self):
		"""Build The Game"""
		self.sm = ScreenManager()
		self.interface = Screen()
		self.interface.add_widget(InterfaceWidget())
		self.sm.add_widget(self.interface)
		return self.sm

class BoxLay(Widget):
	"""Box Layout"""
	def __init__(self, **kw):
		super().__init__(**kw)
		Window.clearcolor = (0.1, 0.1, 0.1, 1)
		self.size = Window.size
		self.ticking = 6
		self.android_im = Image(size = (dp(256), dp(256)))
		self.android_im.pos = (self.center_x-dp(128), self.center_y-dp(128))
		self.android_im.allow_stretch = True
		self.android_im.source = "assets/Android.png"
		self.android_im.texture.mag_filter = "nearest"
		self.label = Label(text="Android Only",font_size = sp(64))
		self.label.pos = (self.center_x-self.label.width/2, self.center_y+dp(148))
		self.exiting = Label(text="Exiting in 5", font_size = sp(24))
		self.exiting.pos = (self.center_x-self.label.width/2, self.center_y-dp(200))
		self.add_widget(self.label)
		self.add_widget(self.android_im)
		self.add_widget(self.exiting)
		Clock.schedule_interval(lambda _: self.tick(), 1)
	
	def tick(self):
		"""Tick"""
		if self.ticking == 0:
			sys.exit()
			return False
		self.ticking -= 1
		self.exiting.text = f"Exiting in {self.ticking}"

if __name__ == "__main__":
	if platform == "android":
		if Window.width < Window.height:
			RPGGameApp().run()
		else: RPGGameApp().run()
	else: runTouchApp(BoxLay())

