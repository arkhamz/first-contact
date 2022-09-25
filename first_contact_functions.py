
import sys
import pygame
import pygame.font

from pygame.sprite import Group
from settings import Settings
from scoreboard import Scoreboard
from game_stats import GameStats
from ship import Ship
from button import Button
from button import MenuButton
from intro_ship import IntroShip

import game_functions as gf

def run_intro():
	#Initialise the game and create a screen object.
	pygame.init()
	
	#Create settings insta,ce intro screen, window caption
	#Create introShip class instance and play the intro music
	game_settings = Settings()
	intro = pygame.display.set_mode((
	game_settings.screen_width, game_settings.screen_height))
	#Add pygame.FULLSCREEN arg after tuple to make it fulscreen
	pygame.display.set_caption("First Contact")
	
	intro_ship = IntroShip(game_settings,intro)
	intro_ship.play_ship_music()
	

	while game_settings.intro_active == True:
		
		for event in pygame.event.get():
			#check if player clicks  cancel or presses q to quit
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
		gf.sleep(1)
		run_menu()

def run_menu():
	
	#Initialise the menu and create a menu screen object.
	pygame.init()
	
	#Create a settings instance, menu screen and get rect coordinates of menu 
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
	
	while game_settings.menu_active != True:
		
		
		gf.check_menu_events(play_b,exit_b)
		
		gf.draw_menu_text(menu)
		play_b.draw_button()
		exit_b.draw_button()
	
		
		pygame.display.flip()

def run_game():
	#Initialise the game and create a screen object.
	pygame.init()
	
	#Play background music
	#pygame.mixer.music.load("bg_music.wav")
	#pygame.mixer.music.play(-1)
	
	game_settings = Settings()
	screen = pygame.display.set_mode((
	game_settings.screen_width, game_settings.screen_height))
		#Add pygame.FULLSCREEN arg after tuple to make it fulscreen
	pygame.display.set_caption("First contact")
	
	#screen2 = pygame.display.set_mode((
	#game_settings.screen_width, game_settings.screen_height))
	#pygame.display.set_caption("First contact")

	
	clock = pygame.time.Clock()

	
	#Make the play button
	play_button = Button(game_settings,screen,"Start")
	
	#Make a GameStats instance and a scoreboard instance
	stats = GameStats(game_settings)
	score = Scoreboard(game_settings,screen,stats)
	
	#make a ship, bullet group and alien group
	ship = Ship(game_settings, screen)
	bullets = Group()
	aliens = Group()

	#create the fleet of aliens
	gf.create_fleet(game_settings, screen,ship, aliens)

	#Start the main loop for the game.
	while True:
		gf.check_events(game_settings,screen,stats,score,play_button,
			ship,aliens,bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(game_settings,screen,stats,score,ship,
				aliens,bullets)
			gf.update_aliens(game_settings,screen,stats,score,ship,
				aliens,bullets)
				
			clock.tick(500)
		
			
		gf.update_screen(game_settings, screen,stats,score,ship,aliens,
			bullets,play_button)
