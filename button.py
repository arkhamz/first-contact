import pygame.font

class Button():

	def __init__(self, game_settings, screen, msg):
		"""Inititalise button attributes"""
	
		self.screen = screen
		self.screen_rect = screen.get_rect()
	
		#Set the dimensions and properties of the button
		self.width, self.height = 200, 50
		self.button_colour = (0,255,0)
		self.text_colour = (255,255,255)
		self.font = pygame.font.SysFont("calibri", 40)
	
		#Build the button's rect object and center it
		self.rect = pygame.Rect(0,0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		self.rect.y += 100
		
		#Prepare the button message, convert it to image and center it
		self.prep_msg(msg)
	
	def prep_msg(self,msg):
		"""Turn message into a rendered image and center it on the button"""
		self.msg_image = self.font.render(
			msg, True, self.text_colour, self.button_colour)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		#draw blank button and draw message
		self.screen.fill(self.button_colour, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

class MenuButton():
	"""A class for representing and handling menu buttons"""

	def __init__(self, game_settings, menu):
		"""Inititalise button attributes"""
		#create menu attribute and create a rect of menu
		self.menu = menu
		self.menu_rect = menu.get_rect()
		#Create message attributes  we will add to buttons as text images
		# Will use these in calls to prep functions
		self.msg1 = "Play Game"
		self.msg2 = "Quit Game"
	
		#Set the button's dimensions and properties
		self.width, self.height = 200, 50
		self.button_colour = (65,146,121)
		#Set a lighter colour for the button which we will switch to
		#if the mouse cursor is on a button
		self.lighter = (98,145,130)
		#set the text colour and create a font for the text
		#we changed font from None to calibri so pyinstaller works
		self.text_colour = (255,255,255)
		self.font = pygame.font.SysFont("calibri", 40)
		
	
	
		#Create a play button rect and center it
		
		self.play_rect = pygame.Rect(0,0, self.width, self.height)
		self.play_rect.center = self.menu_rect.center
		#Create an exit button rect, center it with menu
		#move it down 80 pixels 
		self.exit_rect = pygame.Rect(0,0, self.width, self.height)
		self.exit_rect.center = self.menu_rect.center
		self.exit_rect.y += 80
		
		#Prepares the button message by rendering it as image and centering it
		self.prep_playb(self.msg1)
		self.prep_exitb(self.msg2)
	
	def prep_playb(self,msg):
		"""Convert msg text into an image, centers text image on button """
		#Create image of message text
		self.msg_image1 = self.font.render(msg,
			True, self.text_colour, self.button_colour)
		#create rect of message image
		self.msg_image_rect1 = self.msg_image1.get_rect()
		#use play button rect center to center message image on the button
		self.msg_image_rect1.center = self.play_rect.center	
	
	def prep_exitb(self,msg):
		"""Convert the msg text into an image and center it on button"""
		self.msg_image2 = self.font.render(
			msg, True, self.text_colour, self.button_colour)
		self.msg_image_rect2 = self.msg_image2.get_rect()
		self.msg_image_rect2.center = self.exit_rect.center	
		
	

	def draw_button(self):
		#draw green colour on play & exit button rect on menu
		self.menu.fill(self.button_colour, self.play_rect)
		self.menu.fill(self.button_colour, self.exit_rect)
		#draw msg1 image and msg2 image at their rects/draw positions on screen 
		self.menu.blit(self.msg_image1, self.msg_image_rect1)
		self.menu.blit(self.msg_image2,self.msg_image_rect2)
		
		#Get mouse_x and mouse_y positions
		mouse_x,mouse_y = pygame.mouse.get_pos()
		
		#Check if mouse cursor is over the play button rect 
		#Colour it lighter and re-draw text on top
		if self.play_rect.collidepoint(mouse_x,mouse_y):
		
			self.menu.fill(self.lighter, self.play_rect)
			self.menu.blit(self.msg_image1, self.msg_image_rect1)
		#Check if mouse cursor is over the exit button rect
		#colour it lighter and re-draw text on top	
		if self.exit_rect.collidepoint(mouse_x,mouse_y):
			self.menu.fill(self.lighter, self.exit_rect)
			self.menu.blit(self.msg_image2,self.msg_image_rect2)
