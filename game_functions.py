import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
from game import run_game
from random import randint

def check_events(game_settings,screen,stats,score,play_button,ship,
	aliens,bullets):
	"""respond to general events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#get x and y coordinates of the click area
			mouse_x, mouse_y = pygame.mouse.get_pos()
			#check if the mouse cursor point was on the play button rect
			check_play_button(game_settings,screen,stats,score,
				play_button,ship,aliens,bullets,mouse_x,mouse_y)
			
			
			
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,game_settings,screen,ship,bullets)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
def check_play_button(game_settings,screen,stats,score,play_button,ship,
	aliens,bullets,mouse_x,mouse_y):
	"""Start a new game when the player clicks play."""
	"""and if game_active flag not true"""
	
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#reset the dynamic settings
		game_settings.initialise_dynamic_settings()
		#Hide the mouse cursor
		pygame.mouse.set_visible(False)
	
		#reset game statistics - i.e. ships_left value
		stats.reset_stats()
		stats.game_active = True
		
		#Reset the scoreboard images
		score.prep_score()
		score.prep_high_score()
		score.prep_level()
		score.prep_ships()
		
		#Empty the list(group)of aliens and bullets
		aliens.empty()
		bullets.empty()
		
		#create a new fleet and center the ship
		create_fleet(game_settings,screen,ship,aliens)
		ship.center_ship()
		#play music
		bg_music(game_settings)
		
		
def bg_music(game_settings):
		if game_settings.ship_limit != 0:
			pygame.mixer.music.load("audio/bg_music2.wav")
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play(-1)
		
def check_keydown_events(event,game_settings, screen,ship, bullets):
	"""respond to KEYDOWN"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(game_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""respond to KEYUP"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(game_settings,screen,stats,score,ship,aliens,bullets, 
	play_button):
	"""Update images on the screen"""
	"""redraw screen during each pass through the loop"""
	screen.fill(game_settings.bg_colour)
	#redraw all bullets before drawing  ship n aliens via blitme & draw
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()
	aliens.draw(screen)
	#draw the score information
	score.show_score()
	#Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()
	
	#display the most recently drawn screen
	pygame.display.flip()
	
	
def update_bullets(game_settings,screen,stats,score,ship,aliens,
	bullets):
		bullets.update()
		
		#get rid of bullets that have gone past the screen
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		check_bullet_alien_collisions(game_settings,screen,stats,score,
			ship,aliens,bullets)
			
def check_bullet_alien_collisions(game_settings, screen,stats,score,
	ship,aliens,bullets):
	"""Respond to bullet collisions and re-create fleet if all aliens 
	destroyed"""
	
	#check for any bullets that have hit aliens
	#if so, get rid of the bullets and create new fleet
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		 pygame.mixer.Channel(0).play(pygame.mixer.Sound("audio/hit3.wav"))
		 pygame.mixer.Channel(0).set_volume(1.0)
		 
		 for alien in collisions.values():
			 stats.score += game_settings.alien_points * len(alien)
			 score.prep_score()
			 update_high_score(stats,score)
			 
	if collisions and len(aliens) == randint(1,50):
		#Play wilhelm scream when a collision occurs and the number of 
		#aliens left is a random number
		pygame.mixer.Channel(2).play(pygame.mixer.Sound("audio/scream.wav"))
			
	
	if len(aliens) == 0:
		#If the fleet is destroyed, clear bullets and create new fleet
		#/level
		bullets.empty()
		game_settings.increase_speed()
		
		#increase level count
		stats.level += 1
		score.prep_level()
		
		create_fleet(game_settings, screen, ship, aliens)

def fire_bullet(game_settings, screen, ship, bullets):
	#Fire bullet if spacebar is pressed
	if len(bullets) < game_settings.bullets_allowed:
		new_bullet = Bullet(game_settings, screen, ship)
		pygame.mixer.Channel(1).play(pygame.mixer.Sound("audio/shoot_new.wav"))
		pygame.mixer.Channel(1).set_volume(0.2)
		bullets.add(new_bullet)
		

def get_number_aliens_x(game_settings, alien_width):
	"""determine the number of aliens that fit in a row"""
	available_space_x = game_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x /(2 * alien_width))
	return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
	"""Determine the number of alien rows that fit on the screen"""
	available_space_y = game_settings.screen_height - (3 * alien_height - ship_height)
	number_rows = int(available_space_y/(2 * alien_height))
	return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(game_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + (2 * alien_width * alien_number)
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + (1 * alien.rect.height * row_number)
	aliens.add(alien)

		
def create_fleet(game_settings, screen,ship, aliens):
	"""Create a full fleet/row of aliens"""
	#create an alien instance and find the number of aliens in a row
	alien = Alien(game_settings, screen)
	number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
	number_rows = get_number_rows(game_settings, ship.rect.height, 
		alien.rect.height)
	
	#create the fleets of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#create an alien and place it in the row
			create_alien(game_settings, screen, aliens, alien_number,
				row_number)

def update_aliens(game_settings,screen,stats,score,ship,aliens,bullets):
	"""check if fleet reaches edge of ship"""
	""" update position of  aliens in  fleet"""
	"""check for alien-ship collisions"""
	check_fleet_edges(game_settings, aliens)
	aliens.update()
	
	#look for alien-ship collisions
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(game_settings,screen,stats,score,ship,aliens,bullets)
		
	#look for aliens hitting the bottom of the screen
	check_aliens_bottom(game_settings,screen,stats,score,ship,aliens,
		bullets)

def check_fleet_edges(game_settings, aliens):
		"""Check if  fleet is at an edge and change fleet direction"""
		for alien in aliens.sprites():
			if alien.check_edges():
				change_fleet_direction(game_settings, aliens)
				break
	
def change_fleet_direction(game_settings, aliens):
	"""Drop the entire fleet and change the fleets direction."""
	for alien in aliens.sprites():
		alien.rect.y += game_settings.fleet_drop_speed
	game_settings.fleet_direction *= -1

def ship_hit(game_settings,screen,stats,score,ship,aliens,bullets):
	"""Respond to a ship being hit by an alien/player losing ship."""
	if stats.ships_left > 0:
		#Play death sound
		death = pygame.mixer.Sound("audio/death2.wav")
		death.play(0)
		
		#Decrease the number of ships left
		stats.ships_left -= 1
		
		#update scoreboard
		score.prep_ships()
	
		#Empty the groups of aliens and bullets
		aliens.empty()
		bullets.empty()
	
		#Create a new fleet and centre the ship.
		create_fleet(game_settings,screen,ship,aliens)
		ship.center_ship()
	
		#Pause the game for a moment so the player notices the collision
		sleep(0.5)
		
	if stats.ships_left == 0:
		stats.game_active = False
		#stop music if the player runs out of lives
		pygame.mixer.music.stop()
		pygame.mouse.set_visible(True)
	
def check_aliens_bottom(game_settings,screen,stats,score,ship,aliens,
	bullets):
	"""check if any aliens have reached the bottom of the screen"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(game_settings,screen,stats,score,ship,aliens,
				bullets)
			break
			
def update_high_score(stats, score):
	"""Check current score and update high score"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		score.prep_high_score()
		
		

def check_menu_events(play_b,exit_b):
	
	"""respond to menu events"""
	#Close menu window if user clicks close or presses q
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.K_q:
			sys.exit()
		
		#Get mouse cursor position and respond if  user clicks a button
		if event.type == pygame.MOUSEBUTTONDOWN:
			#get x and y coordinates of the mouse cursor 
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_menu_buttons(play_b,mouse_x,mouse_y,exit_b)

			
def check_menu_buttons(play_b,mouse_x,mouse_y,exit_b):
	"""Start/exit game if play/exit button clicked"""
	#Play_clicked/exit_clicked return true if mouse was on a button
	#rect when a MOUSEBUTTONDOWN event/click occured
	play_clicked = play_b.play_rect.collidepoint(mouse_x, mouse_y)
	exit_clicked = exit_b.exit_rect.collidepoint(mouse_x, mouse_y)
	
	#If play button clicked, mute menu music, delay game for 0.2 secs
	#and run game
	if play_clicked:
		pygame.mixer.music.set_volume(0)
		sleep(0.2)
		run_game()
	if exit_clicked:
		sys.exit()


def draw_menu_text(menu):
	"""Draw downloaded text image to menu"""
	#Load image, get rect, get menu rect
	title = pygame.image.load("images/title.bmp")
	title_rect = title.get_rect()
	menu_rect = menu.get_rect()
	#Center title image rect by menu rect & move it 80 pixels up
	title_rect.centerx = menu_rect.centerx
	title_rect.y = 80
	
	menu.blit(title, title_rect)
	
