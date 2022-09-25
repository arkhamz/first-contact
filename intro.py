import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from intro_ship import IntroShip


import game_functions as gf


def run_intro():
	#Initialise the game and create a screen object.
	pygame.init()
	
	#Create a settings instance
	game_settings = Settings()
	#create an intro display screen/surface
	intro = pygame.display.set_mode((
	game_settings.screen_width, game_settings.screen_height))
	#You can add pygame.FULLSCREEN arg after tuple to make it fulscreen
	#We set the intro screen's caption
	pygame.display.set_caption("First Contact")
	#Create an instance of the IntroShip class and then play music
	intro_ship = IntroShip(game_settings,intro)
	intro_ship.play_ship_music()
	

	while game_settings.intro_active == True:
		#While loop runs as long as the intro state is True
		
		for event in pygame.event.get():
			#check if player clicks x on window or presses q to quit
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
		
		intro_ship.check_intro_ship(game_settings)		
		intro_ship.update_intro_ship()
		intro_ship.blitme()
	
		pygame.display.flip()
		
	while game_settings.menu_active == True:
		run_menu()
		
run_intro()
