from kivy.core.window import Window

if Window.width<Window.height:
	BLOCK_SIZE = 16
	BLOCK_TIMES = 2
	CONTROLLER_SIZE = 60
else:
	BLOCK_SIZE = 16
	BLOCK_TIMES = 2
	CONTROLLER_SIZE = 75
WALK_SPEED = 0.2
RUN_SPEED = 0.1
