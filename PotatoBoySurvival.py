'''
Potato Boy Survival
Created By: Chris Herriman Jr
Goal: Survive as long as possible without losing all 3 lives
'''
### IMPORTS ###
import turtle as trtl #Turtle interface, used for game functionality and visuals, shortened to trtl
import random as rnd #Random, used to randomly generate enemy movements, shortened to rnd
from pygame import mixer #Mixer from the pygame library, used for music loops and sound effects
import os, sys #For pyinstaller


### Makes onefile mode work in pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

### Game Base and Screen Setup ###
trtl.clearscreen()
screen = trtl.Screen()
trtl.title("Potato Boy Survival")
screen.setup(700,700)
#Calls to tkinter
screen._root.resizable(False, False) #Sets the screen to not be resizable
screen._root.iconbitmap(resource_path("potatoBoy.ico")) #Sets up the app icon
#Set background
screen.bgpic(resource_path("bg.gif"))
#Create game_over and set it to false
game_over = False
#Default movement speeds 
player_movement_speed = 15
carrot_movement_speed = 17
#Music Setup
mixer.init()
music_loop = resource_path("musicLoop.wav") #Created by user EEE3333E on freesound.org
game_over_music_loop = resource_path("gameOverMusicLoop.wav") #Modified version of the game loop music
mixer.music.load(music_loop)
mixer.music.play(-1)
#Hit Sound Setup
hit_sound = mixer.Sound(resource_path('hitSound.wav')) #Created by user Sadiquecat on freesound.org

### Function to condense object setup lines ###  
def setup_objects(game_object, object_model, object_x, object_y, start_shown, already_registered):
    game_object.speed(0)
    game_object.hideturtle()
    game_object.penup()
    if not already_registered: #Prevents registering a model twice
        screen.addshape(object_model)
    game_object.shape(object_model)
    game_object.goto(object_x,object_y)
    if start_shown: #Determines if the object being created will be shown to start the ga
        game_object.showturtle()

### Carrot Setup ###
carrots = [] #List to contain enemies
carrot_frames = [resource_path("carrotFrame1.gif"), resource_path("carrotFrame2.gif")]
carrot_frame_state = [True,True,True]
for i in range(3):
    carrots.append(trtl.Turtle()) 
setup_objects(carrots[0],carrot_frames[0],290,290,True,False)
setup_objects(carrots[1],carrot_frames[0],-290,210,True,True)
setup_objects(carrots[2],carrot_frames[0],-290,-290,True,True)
screen.addshape(carrot_frames[1])

### Player Setup ###
player_frame_state = True
player_frames = [resource_path("potatoFrame1.gif"), resource_path("potatoFrame2.gif")]
player = trtl.Turtle()
setup_objects(player,player_frames[0],100,-100,True,False)
screen.addshape(player_frames[1])

### Hearts Setup ###
lives = 3
hearts = []
for i in range(3):
    hearts.append(trtl.Turtle())
setup_objects(hearts[0],resource_path("heart.gif"),-275,275,True,False)
setup_objects(hearts[1],resource_path("heart.gif"),-205,275,True,True)
setup_objects(hearts[2],resource_path("heart.gif"),-135,275,True,True)
screen.addshape(resource_path("damaged.gif")) #Sprite for when the player gets hurt

### Create Timer and Timer Icon ###
#Timer Icon
timer_icon = trtl.Turtle()
setup_objects(timer_icon,resource_path("timer.gif"),135,265,True,False)
#Timer Variable
timer_value = 0

## Pixel Numbers ##
numbers = []
for i in range(10):
    numbers.append(resource_path("PixelNumbers/" + str(i) + ".gif"))
    screen.addshape(numbers[i])
#Create turtles for ones, tens, and hundreds place
digits = []
for i in range(3):
    digits.append(trtl.Turtle())
setup_objects(digits[0],numbers[0],260,265,True,True)
setup_objects(digits[1],numbers[0],220,265,True,True)
setup_objects(digits[2],numbers[0],180,265,True,True)

### Create Game Over Screen
game_over_text = trtl.Turtle()
setup_objects(game_over_text,resource_path("gameOver.gif"),-35,30,False,False)

### Create Survival Time Text ###
survival_time_text = trtl.Turtle()
setup_objects(survival_time_text,resource_path("survivalTime.gif"),-5,-190,False,False)

### New Game Button ###
new_game = trtl.Turtle()
setup_objects(new_game,resource_path("newGame.gif"),0,-280,False,False)
screen.addshape(resource_path("newGamePressed.gif")) #changes to this when New Game is pressed
    
#Make sure everything is appearing on screen
screen.update()

### Player Movement Functions ###
#Moves The Player Right
def right():
    x_cor, y_cor = player.position()
    player.seth(0)
    if check_out_bounds(player_movement_speed, 0, x_cor, y_cor):
        animate_player()
        player.forward(player_movement_speed)

#Moves The Player Up
def up():
    player.seth(90)
    x_cor, y_cor = player.position()
    if check_out_bounds(player_movement_speed, 90, x_cor, y_cor):
        animate_player()
        player.forward(player_movement_speed)

#Moves The Player Left
def left():
    x_cor, y_cor = player.position()
    player.seth(180)
    if check_out_bounds(player_movement_speed, 180, x_cor, y_cor):
        animate_player()
        player.forward(player_movement_speed)

#Moves The Player Down
def down():
    player.seth(270)
    x_cor, y_cor = player.position()
    if check_out_bounds(player_movement_speed, 270, x_cor, y_cor):
        animate_player()
        player.forward(player_movement_speed)

def animate_player():
    global player_frame_state
    player_frame_state = not player_frame_state
    if player_frame_state == True:
        player.shape(player_frames[0])
    else:
        player.shape(player_frames[1])

### Checks If Enemies And/Or The Player Is Out Of Bounds ###
def check_out_bounds(speed, direction, x_cor, y_cor):
    if direction == 90 and y_cor + speed < 330: #Check up
        return True 
    elif direction == 270 and y_cor - speed > -290: #Check down
        return True
    elif direction == 0 and x_cor + speed < 300: #Check right
        return True
    elif direction == 180 and x_cor - speed > -320: #Check left
        return True
    return False

### Enemy Movements [Random] ###
def carrot_movement():
    global carrot_movement_speed
    for i in range(len(carrots)):
        if timer_value < 10:
            random_movement(carrots[i])
        else:
           if carrot_movement_speed != 5 and timer_value >= 10:
               carrot_movement_speed = 5
           follow_player(carrots[i])
        animate_carrot(carrots[i], i)
        check_collision()
    #Checks if the game is over
    #If the game is over, the carrot timer will stop
    if not game_over:
        screen.ontimer(carrot_movement, 50) #restart carrot movement loop

### Random Movement
def random_movement(carrot):
    direction = rnd.randint(0,3) * 90
    x_cor, y_cor = carrot.position()
    #Checks if the move will bring the carrot out of bounds
    if check_out_bounds(carrot_movement_speed, direction, x_cor, y_cor):
        carrot.seth(direction)
        carrot.forward(carrot_movement_speed)

### Move Towards Player AI ###
# Effective speed is 1.41x speed
def follow_player(carrot):
    if player.xcor() > carrot.xcor():
        carrot.seth(0)
        carrot.forward(carrot_movement_speed)
    else:
        carrot.seth(180)
        carrot.forward(carrot_movement_speed)
    if player.ycor() > carrot.ycor():
        carrot.seth(90)
        carrot.forward(carrot_movement_speed)
    else:
        carrot.seth(270)
        carrot.forward(carrot_movement_speed)

def animate_carrot(carrot, carrot_num):
    global carrot_frame_state
    carrot_frame_state[carrot_num] = not carrot_frame_state[carrot_num]
    if carrot_frame_state[carrot_num] == True:
        carrot.shape(carrot_frames[0])
    else:
        carrot.shape(carrot_frames[1])

### Check For Collisions ###
def check_collision():
    player_x, player_y = player.position()
    for i in range(len(carrots)):
        carrot_x, carrot_y = carrots[i].position()
        if (player_x - carrot_x < 45 and player_x - carrot_x > -45) and (player_y - carrot_y < 70 and player_y - carrot_y > -70):
            jump_in_bounds = False
            while not jump_in_bounds:
                direction = rnd.randint(0,3)*90
                jump_in_bounds = check_out_bounds(300, direction, carrot_x, carrot_y)
            carrots[i].seth(direction)
            carrots[i].forward(300)
            damaged()

### Player Damaged ###
def damaged():
    global lives
    if lives > 0:
        lives = lives - 1
        hit_sound.play()
        hearts[lives].shape(resource_path("damaged.gif"))
        if lives == 0:
            stop_game()

### Game Over Sequence ###
def stop_game():
    global game_over
    #Enable game over music loop
    mixer.music.load(game_over_music_loop)
    mixer.music.play(-1)
    #Mark the game as over
    game_over = True
    #Hide hearts
    for i in range(len(hearts)):
        hearts[i].hideturtle()
    #Hide carrots
    for i in range(len(carrots)):
        carrots[i].hideturtle()
    #Hide player
    player.hideturtle()
    #Hide timer icon
    timer_icon.hideturtle()
    #Create game over screen
    game_over_text.showturtle()
    survival_time_text.showturtle()
    digits[0].goto(-125,-198)
    digits[1].goto(-165,-198)
    digits[2].goto(-205,-198)
    #Show new game button
    new_game.showturtle()

### On Screen Timer ###
def update_timer():
    global timer_value
    if not game_over: #Checks to make sure the game is still going
        timer_value += 1
        timer_math = timer_value
        if timer_value <= 999:
            for i in range(len(digits)):
                digits[i].shape(numbers[timer_math % 10])
                timer_math = int(timer_math / 10)
        screen.ontimer(update_timer, 1000) #restart timer loop

### Resets the game to default state ###
def start_new_game(x,y):
    #Global Variables for this method
    global game_over
    global lives
    global timer_value
    global carrot_movement_speed
    #Change NewGame to the pressed color
    new_game.shape(resource_path("newGamePressed.gif"))
    #Hide objects shown during end screen
    new_game.hideturtle()
    new_game.shape(resource_path("newGame.gif"))
    game_over_text.hideturtle()
    survival_time_text.hideturtle()
    #Place hearts back on the screen
    for i in range(len(hearts)):
        hearts[i].showturtle()
        hearts[i].shape(resource_path("heart.gif"))
    lives = 3
    #Place the carrots back on the screen
    for i in range(len(carrots)):
        if i == 0:
            carrots[i].goto(290,290)
        elif i == 1:
            carrots[i].goto(-290,210)
        elif i == 2:
            carrots[i].goto(-290,-290)
        carrots[i].showturtle()
    carrot_movement_speed = 17
    #Add the player back to the screen
    player.showturtle() 
    player.goto(100,-100)
    #Add the timer and clock back to the screen
    timer_icon.showturtle()  
    timer_value = 0
    for i in range(len(digits)):
        digits[i].shape(resource_path("PixelNumbers/0.gif"))
    digits[0].goto(260, 265)
    digits[1].goto(220, 265)
    digits[2].goto(180, 265)
    #Restart carrot movement and clock timer
    screen.ontimer(update_timer, 1000)
    screen.ontimer(carrot_movement, 50)
    #Enable main music loop
    mixer.music.load(music_loop)
    mixer.music.play(-1)
    #Disable gameOver variable
    game_over = False

#Looks for key presses
screen.listen() 

### Key Presses For Player Movement ###
#Up Movements
screen.onkey(up, "Up")
screen.onkey(up, "w")

#Left Movements
screen.onkey(left, "Left")
screen.onkey(left, "a")

#Right Movements
screen.onkey(right, "Right")
screen.onkey(right, "d")

#Down Movements
screen.onkey(down, "Down")
screen.onkey(down, "s")

### Button press for a new game ###
new_game.onclick(start_new_game)
        
### Timers ###
#Carrot Movement Timer
screen.ontimer(carrot_movement, 50)

#On Screen Timer
screen.ontimer(update_timer, 1000)

### End of Main Loop ###
trtl.Screen().mainloop()

'''
Possible Updates for Future Versions:
     -Add animations for characters
         -Back frames for carrot
         -Back and maybe side frames for player
     -Add broccoli guy and pepper kid 
        ->Pepper gives short speed boost, but shows up only once every so often
        ->Brocoli gives a heart, but only appears when at 1 heart
'''