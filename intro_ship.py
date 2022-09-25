import pygame
from pygame.sprite import Sprite

class IntroShip(Sprite):
	"""A class that will represent the ship we display on the intro
	screen"""
	
	def __init__(self,game_settings,intro):
		"""Initialise the ship and set its starting position"""
		super(IntroShip, self).__init__()
		self.intro = intro
		self.game_settings = game_settings
		
		#Load the ship image, get shipr ect and screen rect
		self.image = pygame.image.load("images/ship10.bmp")
		self.rect = self.image.get_rect()
		self.intro_rect = intro.get_rect()
		
		#Start each new ship at the bottom centre of the screen
		
		self.rect.centerx = self.intro_rect.centerx
		self.rect.bottom = self.intro_rect.bottom


		#set Y attribute
		self.y = float(self.rect.y)
		

	def update_intro_ship(self):
		"""Move the intro ship up the screen"""
		self.y -= 0.25
		self.rect.y = self.y
	
	def check_intro_ship(self,game_settings):
		"""respond if ship moves of intro screen"""  
		#checks if the ship has passed the intro screen
		if self.rect.bottom == self.intro_rect.top:
			#Paint the screen black to hide the ship
			self.intro.fill(self.game_settings.bg_colour)
			#Set the menu state setting to True so menu can be triggered
			#later
			game_settings.menu_active = True
			#set intro state to False so the intro screen doesnt trigger
			game_settings.intro_active = False
	
	def blitme(self):
		"""Draw the ship at its current location."""
		self.intro.blit(self.image, self.rect)
		

	def play_ship_music(self):
		"""Plays  music as the intro ship flies up the screen"""
		pygame.mixer.music.load("audio/whoosh.wav")
		pygame.mixer.music.set_volume(0.5)
		pygame.mixer.music.play(0)
		
