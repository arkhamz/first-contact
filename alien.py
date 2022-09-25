import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class that represents a single alien in a fleet"""


	#we will pass Alien game settings and relevant screen to display alien on
	def __init__(self, game_settings, screen):
		"""Initialise the alien and set its start position"""
		super(Alien, self).__init__()
		self.screen = screen #set screen property on instances
		self.game_settings = game_settings #set settings on instances
		
		#Load the alien image and create its rect attribute
		self.image = pygame.image.load("images/alien_5.bmp")
		self.rect = self.image.get_rect()
		#Images and screens don't have position by default
		# get_rect() creates a new rect obj with the size of the image and x,y coords of (0,0). 
		
		#start each new alien near the top-left of the screen
		self.rect.x = 0
		self.rect.y = 0
		
		#store the alien's exact horizontal position in a decimal
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""Draw the alien to the screen at its current location"""
		self.screen.blit(self.image, self.rect)
	
		
	def update(self):
		"""Move the alien to the right"""
		self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
		self.rect.x = self.x

	def check_edges(self):
		"""Return True if alien is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
	
