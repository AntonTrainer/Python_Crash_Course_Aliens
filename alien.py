import pygame 
from pygame.sprite import Sprite
from random import randint as rint


class Alien(Sprite): #A class that represents a single alien in the fleet 
    def __init__(self, ai_settings, screen):
        #initialize the alien and set its starting position 
        super(Alien, self).__init__()
        self.screen = screen 
        self.ai_settings = ai_settings

        #load the alien image (women.bmp) and set its rect attribute
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()

        #Start each new alien in the top left corrner of the screen 
        self.rect.x = self.rect.width + rint(-20, 20) #sets the x position one "width" unit i.e. the width of the image rigtht of the left edge of the screen 
        self.rect.y = self.rect.height #sets the y position one "height" unit i.e. the height of the image below the top of the screen 

        #store the aliens exact position 
        self.x = float(self.rect.x) #sets the position to the self.rect.x position (changes as it moves)

    def blitme(self): #pygame for showing the immage 
        self.screen.blit(self.image, self.rect) #shows the image in the self rect position 

    def check_edges(self): #return true if alien is at the edge of the screen 
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: #if the right edge of the alien is past the right edge of the screen 
            return True 
        elif self.rect.left <= 0: # if the left edge of the alien is past the left edge of the screen aka 0 
            return True 

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction # move the alien to the right at the speed factor rate 
        self.rect.x = self.x #the location of the alien will be chagning based on the above criteria 



 