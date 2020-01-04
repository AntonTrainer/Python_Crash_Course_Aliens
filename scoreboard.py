import pygame.font
from pygame.sprite import Group 
from ship import Ship

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        #initialize the score keeping attributes 
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #font settings for the scoreboard
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prep the initial scoreboard image 
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        #turn the score into a rendered image to display with the above settings
        rounded_score = int(round(self.stats.score, -1)) #tells python to round the score to the nearest 10 and store that in rounded_score calling int is really only for python 2.7 or it would print a decimal
        score_str = "{:,}".format(rounded_score) #Adds commas to the rounded score in 3's is 1000 = 1,000 
        self.score_image = self.font.render (score_str, True, self.text_color, self.ai_settings.bg_color)

        #display the score at the top right corner of the screen 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #Set the score board image 20 pixels left of the right edge of the screen 
        self.score_rect.top = 20 

    #turn the high score into a rendered image 
    def prep_high_score(self): 
        high_score = int(round(self.stats.high_score, -1)) 
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        #center the high score 
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10 
    
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10 
            self.ships.add(ship)

    #draw the score board to the screen
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect) #show the score 
        self.screen.blit(self.high_score_image, self.high_score_rect) #display the high score
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen) 

