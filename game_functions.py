import sys
from time import sleep
import pygame 
from settings import Settings 
from ship import Ship
from bullet import Bullet
from alien import Alien
 

def check_keydown_event(ev, ai_settings, screen, ship, bullets):
    #movement events 
    if ev.type == pygame.KEYDOWN:  #move the ship when keys are pressed down
        if ev.key == pygame.K_RIGHT: #if right arrow is pressed
            ship.moving_right = True  #true will make the ship move because the stationary on ship.py is false
        elif ev.key == pygame.K_LEFT: #if left arrow is pressed
            ship.moving_left = True #true will make the ship move because the stationary on ship.py is false
        elif ev.key == pygame.K_SPACE:
             fire_bullet(ai_settings, screen, ship, bullets)
        elif ev.key == pygame.K_q:
            sys.exit()
            
def check_keyup_event(ev, ship):
    if ev.type == pygame.KEYUP: #Detect keys being released   
        if ev.key == pygame.K_RIGHT: #right key up 
            ship.moving_right = False #return ship.py movement flag to false = stationary
        elif ev.key == pygame.K_LEFT: #left key up 
            ship.moving_left = False  #return ship.py movement flag to false = stationary

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets): #checks for all events 
    ev = pygame.event.poll() #looks for any event  
    if ev.type == pygame.QUIT: #Defines the event as clicking the close button on the window  
        sys.exit()  #quit game on exit commend
    elif ev.type == pygame.MOUSEBUTTONDOWN: #when mouse button is pressed
        mouse_x, mouse_y = pygame.mouse.get_pos() #gather the position of the pointer when click is detected
        check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y) #sends to check_play_button function to see if clicked the play button 
    elif ev.type == pygame.KEYDOWN: #calls on key_down_event to see what to do 
        check_keydown_event(ev, ai_settings, screen, ship, bullets)
    elif ev.type == pygame.KEYUP: #calls on key_up_event to see what to do
        check_keyup_event(ev, ship) #the key up events ev and ship are the only keyup events

def check_play_button(ai_settings, screen,stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y): 
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) # if the pointer clicks the button
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False) #set the cursor to invisible when play button clicked i
        stats.reset_stats() #reset the game stats when a new game is started
        stats.game_active = True #start the game
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty() #empty the alien list 
        bullets.empty() # empty the bullet list
        create_fleet(ai_settings, screen, ship, aliens,) #create a new fleet 
        ship.center_ship()#center the ship 
        
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button): #update the screen as things occur, run this through the loop on feminist_invasion.py
    screen.fill(ai_settings.bg_color) #runs the bg_color from settings through the loop
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() # draws the ship image to the screen 
    aliens.draw(screen) #draws the aliens in the group aliens onto the screen after the ship is added
    sb.show_score() #draw the scoreboard and update everytime the loop runs  
    if not stats.game_active: #draw the button if the game is not active, ie when the game is first started 
        play_button.draw_button()
    pygame.display.flip() #makes the most recently defined screen (including all the new events) visable 
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets): #on screen and in group bullet functions 
    bullets.update()
    for bullet in bullets.copy(): #for bullets that are in the list (added as soon as created)
        if bullet.rect.bottom <= 0: # if the bottom of the bullet passes the top of the screen 
            bullets.remove(bullet) #delete the bullet that passes the top of the screen 
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) #Check for collisions between the bullets and the alines then make the alien dissapear
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score() #calling a new image for the scoreboard so it updates with the correct score 
        check_high_score(stats, sb) #checking if the current hit made a new high score 
    if len(aliens) == 0: #if there are no more aliens on the screen 
        bullets.empty() # clear all bullets
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets): #fire bullet function
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width): #define the total number of aliens the cqn fit in a row 
    available_space_x = ai_settings.screen_width - 2 * alien_width #the available space for aliens and how many aliens will fit into that space 
    number_aliens_x =int(available_space_x / (2 * alien_width)) #the number of full size aliens (full size through the int function ehich effectively rounds down the number of aliens that will fit to the next round number) that will fit in a row 
    return number_aliens_x # returns the total number the will fit in a row 

def get_number_rows(ai_settins, ship_height, alien_height): # determine the number of rowns that fit on the screen vertically 
    available_space_y = (ai_settins.screen_height - (3 * alien_height) - (ship_height)) # determines the available space vertically 
    number_rows = int(available_space_y / ( 2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen) #create alien to perform calcs with but doesnt get added to the fleet 
    alien_width = alien.rect.width #set the initial alien width to the rect.width as defined in alien above 
    alien.x = alien_width + 2 * alien_width * alien_number  #set the aliens x value to place it in a row 
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) #add the alien you just made to the group aliens 

def create_fleet(ai_settings, screen, ship, aliens): #create a fleet on aliens 
    alien = Alien(ai_settings, screen) 
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)  
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x): #create the first row of aliens 
            create_alien(ai_settings, screen, aliens, alien_number, row_number) #create an alien 

def check_fleet_edges(ai_settings, aliens): #respond when an alien touches a screen edge
    for alien in aliens.sprites(): 
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens): #drop the entire fleet and change directions 
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed #drop at the speed defined in ai_settings 
    ai_settings.fleet_direction *= -1 

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets): #respond to ship being hit by aliens
    if stats.ships_left >= 1 :
        stats.ships_left -= 1  #reduce ships left when hit 
        aliens.empty() #empty aliens after hit 
        bullets.empty() #empty bullets after hit
        create_fleet(ai_settings, screen, ship, aliens) # create a new flee
        sb.prep_ships() 
        ship.center_ship() #center the new ship 
        sleep(.5) #pause game 
        print("he wasnt readyyyyyyyyyyyyyyyy") 
        print(stats.ships_left)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True) # make the cursor reappear when the game is over 
        print("game over") 
        print(stats.ships_left)
        
def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets): #checking for aliens hitting the bottom 
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets) #react the same as if your ship was hit
            break 
        
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets): #update the aliens, called in the game loop 
    check_fleet_edges(ai_settings, aliens)  #checking if the fleet is at an egde then updating the fleet, as the fleet shrinks the aliens will have to move farther to trigger 
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens): #if there are any collisions run ship hit 
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb): #checking if the current score is a new high score 
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

