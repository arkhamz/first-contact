class GameStats():
	"""A class that tracks statistics for First Contact"""
	
	def __init__(self, game_settings):
		"""Inititalise statistics"""
		self.game_settings = game_settings
		self.reset_stats()
		
		#Game high score
		self.high_score = 0
		
		#Start First contact in an active state
		self.game_active = False

		
	def reset_stats(self):
		"""Inititalise statistics that can change during the game."""
		self.ships_left = self.game_settings.ship_limit
		self.score = 0
		self.level = 1
