from game_stats import GameStats

class Settings():  #Creates a class to store all the alienn invasion settings 
    def __init__(self):  #Initialize the game settings 
        self.screen_width = 1500 #window width 
        self.screen_height = 750 #window hight 
        self.bg_color = (100, 200, 0) #background color 
        self.ship_speed_factor = 6 #ship speed 
        self.ship_limit = 3 # number of "lives"

        #bullet settings 
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 100, 20, 20 
        self.bullets_allowed = 10

        #alien settings
        self.alien_speed_factor = .9  
        self.fleet_drop_speed = 8 # how fast the aliens work down the screen per line 
        self.fleet_direction = 1 # 1 moves right and -1 moves the fleet left 

        #speeding up with levels 
        self.speedup_scale = 1.5 #how much faster per level 
        self.score_scale = 1.5 #increasing the point value of each alien by a factor of 1.5 each level
        self.initialize_dynamic_settings() #what needs to change when we speed up 

    #defining what will change throughout the game
    def initialize_dynamic_settings(self):  
        self.ship_speed_factor = 4 
        self.bullet_speed_factor = 5 
        self.alien_speed_factor = .85 
        self.fleet_direction = 1
        self.alien_points = 50 #each alien will be worth 50 points at the begining of the game 

    #increasing speed settings 
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

