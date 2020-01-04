#Stats for Alien Invasion
class GameStats(): #Track statistics for alien invasion game 
    def __init__(self, ai_settings): #initialize statistics 
        self.ai_settings = ai_settings 
        self.reset_stats()
        self.game_active = False #start game in an inactive state so a play button can activate it 
        self.high_score = 0 # high score should never be reseet 

    def reset_stats(self): #initializes stats that can change during the game 
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = True # start the game in an active state 
        self.score = 0 
        self.level = 1 