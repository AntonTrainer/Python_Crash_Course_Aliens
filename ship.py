import pygame
from settings import Settings
from pygame.sprite import Sprite 


class Ship(Sprite):
    def __init__(self, ai_settings, screen): #initiallizes the ship
        super(Ship, self).__init__() 
        self.screen = screen 
        self.ai_settings = ai_settings

        #loads the image ship and get its rect insert the path to the image on self.image 
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #starting postion settings 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.moving_right = False #movement right flag
        self.moving_left = False #left movement flag 

    def update(self): #update the ship postion based on movement flag 
        if self.moving_right and self.rect.right < self.screen_rect.right:#stop movement at right boundary
            self.center += self.ai_settings.ship_speed_factor #move right by updating the ships center value not the rect 
        if self.moving_left and self.rect.left > self.screen_rect.left: #stop movement at left boundary can also do "and self.rect.left > 0:"
            self.center -= self.ai_settings.ship_speed_factor#move left by updating the ships center value not the rect
        self.rect.centerx = self.center #update rect object from self.center 

    def blitme(self):
        self.screen.blit(self.image, self.rect) #draw the stuff at its current location 

    def center_ship(self): #center the ship on the screen, for use when new ship or level 
        self.center = self.screen_rect.centerx
