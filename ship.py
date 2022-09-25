import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self,game_settings,screen):
		"""Initialise the ship and set its starting position"""
		super(Ship, self).__init__()
		self.screen = screen
		self.game_settings = game_settings
		
		#Load the ship image, get shipr ect and screen rect
		self.image = pygame.image.load("images/ship10.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Start each new ship at the bottom centre of the screen
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.center = float(self.rect.centerx)
		
		#Movement flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""update the ship's position if the movement flag is set to True
		and stop the ship going off the left or right side."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.game_settings.ship_speed_factor
		if self.moving_left and self.rect.left >0:
			self.center -= self.game_settings.ship_speed_factor
		
		#update the rect attribute with the self.center value
		self.rect.centerx = self.center
		

		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
	
	def center_ship(self):
		"""center the ship on the screen."""
		self.center = self.screen_rect.centerx
