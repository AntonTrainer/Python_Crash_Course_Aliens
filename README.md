# Python Crash Course Alien Invasion Game
Alien Invasion game that was created in *Python Crash Course* by Eric Matthes 

### See dependancies.txt  
  *all scripts written in VS Code and run on Windows machine.*

## Playing the game:
#### *alien_invasion.py* is the script that runs the game and creates several important objects that are going to be used throughout the game. This is the only script that needs to be run to play the game. 

### Modules 
*settings.py* contains the Settings class that alien_invasion.py relies upon.
*game_functions.py* contains small functions that run constantly throughout the game and carry out most of the work such as controlling the ship.
*game_stats.py* keeps track of all the game statistics.
*scoreboard.py* creates the Scoreboard class to display the score that is contained in game_stats.py

*button.py* because Pygame does not have a built-in method to make buttons, you can crease a filled in rectangle with a label to create buttons such as "Start" or "New Game."

*ship.py* contains the Ship class. Stores the ship's location and calls the ship.bmp file.
*alien.py* similar to ship.py

### Image Files
*alien.bmp*
*ship.bmp*

Note: There may be spelling errors and unneccassary lines and imports throughout
