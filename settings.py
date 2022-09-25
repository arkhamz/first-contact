

class Settings():
	"""A class that stores all settings for Alien Invasion."""
	
	def __init__(self):
		"""Inititalise The game's static settings"""
		#Our screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_colour = (0, 0, 0)
		#60 colour for each is black
		#230 for each is grey
		#ship settings
		self.ship_limit = 3
	
		
		#bullet settings
		self.bullet_width = 4
		self.bullet_height = 15
		self.bullet_colour = 255, 165, 0
		self.bullets_allowed = 3
		
		#alien settings
		self.fleet_drop_speed = 9
		
		#game state settings
		self.intro_active = True
		self.menu_active = False
		
	
		
		#How quickly the game speeds up
		self.speedup_scale = 1.1
		self.initialise_dynamic_settings()


	def initialise_dynamic_settings(self):
		"""Initialise settings that change throughout the game"""
		self.ship_speed_factor = 0.8
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.7
		self.alien_points = 50
		
		#fleet direction of 1 represents right, -1 represents left
		self.fleet_direction = 1
		
	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
	
	
