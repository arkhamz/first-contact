import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class that represents ship bullet and its properties"""
	
	def __init__(self, game_settings, screen, ship):
		"""create a bullet object at the ship's current position"""
		super(Bullet, self).__init__() #Bullet inherits from Sprite
		self.screen = screen
		
		#Create a bullet rect at (0,0) and set its position
		self.rect = pygame.Rect(
			0,0, game_settings.bullet_width, game_settings.bullet_height
			)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#Store the bullet's y coordinate/position as a decimal value
		self.y = float(self.rect.y)
		
		self.colour = game_settings.bullet_colour
		self.speed_factor = game_settings.bullet_speed_factor
		
	def update(self):
		"""move the bullet up the screen."""
		#update the bullet's movement
		self.y -= self.speed_factor
		#update the rect's y attribute value
		self.rect.y = self.y
			
	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.colour, self.rect)
