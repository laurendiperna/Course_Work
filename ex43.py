#ex43
class Scene(object):

	def enter(self):
		pass
		
class Engine(object):

	def __init__(self, scene_map):
		pass
		
	def play(self):
		pass
		
class Death(Scene):
	"""This is when the player dies and should be something funny"""
	
	def enter(self):
		pass
		
class CentralCorridor(Scene):
	"""This is the starting point and has a Gothon already standing there 
	they have to defeat with a joke before continuing"""

	def enter(self):
		pass
		
class LaserWeaponArmory(Scene):
	"""This is where the hero gets a neutron bomb to blow up the ship
	before getting to the escape pod. It has a keypad the hero has to guess
	the number for."""
	
	def enter(self):
		pass
		
class TheBridge(Scene):
	"""Another battle scene with a Gothon where the hero places the bomb."""
	
	def enter(self):
		pass
		
class EscapePod(Scene):
	"""Where the hero escapes but only after guessing the right escape pod"""
	
	def enter(self):
		pass
		
class Map(object):
	
	def __init__(self, start_scene):
		pass
		
	def next_scene(self, scene_name):
		pass
		
	def opening_scene(self):
		pass
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()