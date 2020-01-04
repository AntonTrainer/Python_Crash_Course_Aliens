import pygame.font 

class Button():
    def __init__(self, ai_settings, screen, msg): #initialize button attributes 
        self.screen = screen 
        self.screen_rect = screen.get_rect()

        #set the dimensions of the button
        self.width, self.height = 200,50
        self.button_color = (255, 0 ,0)
        self.text_color = (255 ,255 , 255)
        self.font = pygame.font.SysFont(None, 48) #prepare a font attribute in pygame for rendering text none means default text and 48 is the size 

        #build the button rect and center the button 
        self.rect = pygame.Rect(0, 0, self.width, self.height) # set the buttons center attribute to the center of the screen
        self.rect.center = self.screen_rect.center 

        #the button message 
        self.prep_msg(msg)
    
    def prep_msg(self, msg): #turning the messafe into an image and centering it on the button
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #turns the font stored in msg into an image, font.render turns on/off antialiasing to make text edges smoother 
        self.msg_image_rect = self.msg_image.get_rect() 
        self.msg_image_rect.center = self. rect.center 
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect) #draw the button background
        self.screen.blit(self.msg_image, self.msg_image_rect) #draw the text on the background

    

    