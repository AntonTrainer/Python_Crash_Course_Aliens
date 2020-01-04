import sys
import pygame 
from settings import Settings 
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button 
from scoreboard import Scoreboard

def run_game():
    #initialize game and create screen object, are default commands to set the pygame up 
    pygame.init() #start pygame
    ai_settings = Settings() #defining ai_settings as the Settings() that were imported 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #size of the game window 
    pygame.display.set_caption("Alien Invasion") #window caption 
    play_button = Button(ai_settings, screen, "play") #build the paly button 
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    alien = Alien(ai_settings, screen) #makes the alien
    ship = Ship(ai_settings, screen) #call the ship from Ship.py
    bullets = Group() # make a group to store bullets in 
    aliens = Group() #make a group to store the aliens in until they are shot down
    gf.create_fleet(ai_settings, screen, ship, aliens) # creare the fleet of aliens
    
    while True:  #build the loop to run the game 
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) 
        if stats.game_active:
            ship.update() #updating the ship when the loop updates 
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) #running the update_bullet function through the loop  
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets) #running update_aliens through the loop  
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  #Displays the above window 

run_game() #runs the game window 

input()
