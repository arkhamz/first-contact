import sys
import pygame
import pygame.font

from settings import Settings
from button import MenuButton
import game_functions as gf

def run_menu():
	
	#Initialise the menu and create a menu screen object.
	pygame.init()
	
	#Create a settings instance and menu screen surface 
	game_settings = Settings()
	menu = pygame.display.set_mode((
	game_settings.screen_width, game_settings.screen_height))
	menu_rect = menu.get_rect()
	#Add pygame.FULLSCREEN arg after tuple to make it fulscreen
	pygame.display.set_caption("First Contact")
	
	play_b = MenuButton(game_settings,menu)
	exit_b = MenuButton(game_settings,menu)
	
	pygame.mixer.music.load("audio/menu.wav")
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(0)
	
	while game_settings.menu_active == True:
		#Remember that running through the intro sets this to True
		
		
		gf.check_menu_events(play_b,exit_b)
		
		gf.draw_menu_text(menu)
		play_b.draw_button()
		exit_b.draw_button()
	
		
		pygame.display.flip()
		
run_menu()
