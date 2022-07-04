"""Interface"""
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.metrics import dp
from widgets import MessageBox

from configuration import BLOCK_SIZE, BLOCK_TIMES
from character import Player, NPC, PlayerHead
from all_world import World1_0
from controllers import (
	UpButton, LeftButton, DownButton,
	RightButton, BButton, AButton,
)

class InterfaceWidget(Widget):
	"""Interface Widget"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.size = Window.size
		self.all_variables()
		self.display_player()
		self.display_field()
		self.widgets()
		self.all_controller()

	def all_variables(self):
		"""All Variable"""
		self.block_size = dp(BLOCK_SIZE*BLOCK_TIMES)
		self.player_position = (5, 5)
		self.pos_row = self.player_position[0]
		self.pos_col = self.player_position[1]
		self.all_npc_position = list()
		self.all_npc_list = list()
		self.look_position = "down"
		self.walk_up = False
		self.walk_down = False
		self.walk_left = False
		self.walk_right = False
		self.touched = False
		self.running = False
	
	def display_player(self):
		"""Display Player"""
		self.player = Player()
		self.player_head = PlayerHead()
		self.player_head.y = self.player.y+(self.block_size-(dp(BLOCK_TIMES-(BLOCK_TIMES/10))))

	def display_field(self):
		"""Display Field"""
		self.world_1_0 = World1_0()
		self.world_1_0.pos = self.player.pos
		self.world_1_0.y -= self.block_size*(self.world_1_0.world_size[1]-1)
		self.world_1_0_upper = Image()
		self.world_1_0_upper.source = "assets/world/upper_1_0.png"
		self.world_1_0_upper.allow_stretch = True
		self.world_1_0_upper.texture.mag_filter = "nearest"
		self.world_1_0_upper.size = self.world_1_0.size
		self.world_coordinate = Label(pos = (100, Window.height-100))
		self.current_world = self.world_1_0
		self.current_world_upper = self.world_1_0_upper
		self.current_world_pos = self.world_1_0.pos
		self.relocate_player()
		self.display_background()

	def display_background(self):
		"""Display Background"""
		self.bg_texture = Image(source="assets/bg.png").texture
		self.bg_texture.wrap = "repeat"
		self.bg_texture.uvsize = (50, 50)
		self.bg_texture.mag_filter = "nearest"
		self.bg_texture.flip_vertical()
		with self.canvas:
			self.x_pos = (100-self.current_world.world_size[1])//2
			self.y_pos = (100-self.current_world.world_size[0])//2
			if self.x_pos % 2: self.x_pos+=1
			if self.y_pos % 2: self.y_pos+=1
			self.bg_1 = Rectangle()
			self.bg_1.size = (100*self.block_size, 100*self.block_size)
			self.bg_1.pos = (self.current_world.x-(self.block_size*self.x_pos),
				self.current_world.y-(self.block_size*self.y_pos))
			self.bg_1.texture = self.bg_texture
			self.current_bg = self.bg_1

	def current_position_bind(self, _, pos):
		"""Bind Position"""
		self.current_world_upper.pos = pos
		self.current_bg.pos = (pos[0]-(self.block_size*self.x_pos),
			pos[1]-(self.block_size*self.y_pos))
		for widget in self.all_npc.children:
			self.npc_position(widget, *widget.position, widget.mover_x, widget.mover_y)

	def relocate_player(self):
		"""Relocate Player"""
		self.current_world.x -= self.block_size*self.player_position[1]
		self.current_world.y += self.block_size*self.player_position[0]
		self.world_1_0_upper.pos = self.world_1_0.pos
		self.current_world.bind(pos = self.current_position_bind)

	def npc_position(self, widget, row=0, col=0, x=0, y=0):
		"""Npc Position"""
		pos_x = self.current_world_pos[0]+(self.block_size*col)
		pos_y = (self.current_world_pos[1]+self.block_size*
		(self.world_1_0.world_size[1]-1))-(self.block_size*row)
		widget.pos = (pos_x+x, pos_y+y)

	def update_coordinate(self):
		"""Update Coordinate"""
		self.world_coordinate.text = f"{self.pos_row}, {self.pos_col}"

	def widgets(self):
		"""Widgets"""
		self.add_widget(self.world_1_0)
		self.add_widget(self.player)
		self.display_all_npc()
		self.add_widget(self.player_head)
		self.add_widget(self.world_1_0_upper)
		self.add_widget(self.world_coordinate)
	
	def display_all_npc(self):
		"""All Npc"""
		self.all_npc = Widget()
		self.all_npc_list.append(NPC((14,11), "assets/character/npc1/down.png",
			"", 1))
		self.all_npc.add_widget(self.all_npc_list[0])
		self.all_npc_position.append((14, 11))
		self.all_npc_list.append(NPC((14,8), "assets/character/npc1/down.png",
			"random", 2, ""))
		self.all_npc.add_widget(self.all_npc_list[1])
		self.all_npc_position.append((14, 8))
		self.add_widget(self.all_npc)

	def all_controller(self):
		"""All Controller"""
		trans = 0.4
		self.up_button = UpButton(opacity=trans)
		self.left_button = LeftButton(opacity=trans)
		self.down_button = DownButton(opacity=trans)
		self.right_button = RightButton(opacity=trans)
		self.b_button = BButton(opacity=trans)
		self.a_button = AButton(opacity=trans)
		self.readd_controller()
	
	def message_box(self):
		"""Add Message Box"""
		self.reremove_controller()
		self.message_box_1 = MessageBox()
		self.add_widget(self.message_box_1)
		#self.test = Label()
#		self.test.color = (1,0,0,1)
#		self.test.text = "Test"
#		self.test.pos = self.message_box_1.pos
#		self.test.x += dp(20)
#		self.test.y += self.message_box_1.height/2
#		self.add_widget(self.test)
		self.readd_controller()

	def remove_message_box(self):
		"""Remove Message Box"""
		self.remove_widget(self.message_box_1)

	def reremove_controller(self):
		"""Remove Controller"""
		self.remove_widget(self.up_button)
		self.remove_widget(self.left_button)
		self.remove_widget(self.down_button)
		self.remove_widget(self.right_button)
		self.remove_widget(self.b_button)
		self.remove_widget(self.a_button)
	
	def readd_controller(self):
		"""Add Controller"""
		self.add_widget(self.up_button)
		self.add_widget(self.left_button)
		self.add_widget(self.down_button)
		self.add_widget(self.right_button)
		self.add_widget(self.b_button)
		self.add_widget(self.a_button)
