import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite): #creates a class to manage the bullets 

#create a bullet and put it at the ships current position 
    def __init__(self, ai_settings, screen, ship): 
        super(Bullet, self).__init__() 
        self.screen = screen #put the bullet on the screen 

        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height) #create a bullet on the settings size at 0,0
        self.rect.centerx = ship.rect.centerx  #put the bullet center of the rect aka the ship
        self.rect.top = ship.rect.top #put the bullet at the top up the rect aka the ship

        self.y = float(self.rect.y) #store the bullets y position as a decimal under self.y 
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''moving the bullet up the screen'''
        self.y -= self.speed_factor #update the decimal position of the bullet
        self.rect.y = self.y #update the rect position 

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet to the screen 

