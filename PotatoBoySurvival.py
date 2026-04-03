### IMPORTS ###
import turtle as trtl #Turtle interface, used for game functionality and visuals, shortened to trtl
import random as rnd #Random, used to randomly generate enemy movements, shortened to rnd

### Screen Setup ###
trtl.clearscreen()
screen = trtl.Screen()
trtl.title("Potato Boy Survival")
screen.setup(700,700)
screen._root.resizable(False, False)
screen.bgpic("bg.gif")
Font = ("Monospace", 50)
gameOver = False
playerMovementSpeed = 15
CarrotMovementSpeed = 17

### Carrot Setup ###
# Before player setup so that the player will apear above the carrots on the screen #
screen.addshape("carrotMan.gif")
carrots = []    
for i in range(3):
    carrots.append(trtl.Turtle())
    carrots[i].speed(0)
    carrots[i].hideturtle()
    carrots[i].shape("carrotMan.gif")
    carrots[i].penup()
    if i == 0:
        carrots[i].goto(290,290)
    elif i == 1:
        carrots[i].goto(-290,210)
    elif i == 2:
        carrots[i].goto(-290,-290)
    carrots[i].showturtle()

### Player Setup ###
screen.addshape("potatoBoy.gif")
Player = trtl.Turtle()
Player.shape("potatoBoy.gif")
Player.penup()
Player.speed(0)
Player.goto(100,-100)

### Hearts Setup ###
screen.addshape("heart.gif")
screen.addshape("damaged.gif")
lives = 3
hearts = []
for i in range(3):
    hearts.append(trtl.Turtle())
    hearts[i].speed(0)
    hearts[i].hideturtle()
    hearts[i].penup()
    hearts[i].shape("heart.gif")
    if i == 0:
        hearts[i].goto(-275,275)
    elif i == 1:
        hearts[i].goto(-205,275)
    else:
        hearts[i].goto(-135,275)
    hearts[i].showturtle()

### Create Timer and Timer Icon ###
#Timer Icon
screen.addshape("timer.gif")
TimerIcon = trtl.Turtle()
TimerIcon.hideturtle()
TimerIcon.speed(0)
TimerIcon.shape("timer.gif")
TimerIcon.penup()
TimerIcon.goto(135,265)
TimerIcon.showturtle()

#Timer Variable
timer = 0

#Timer Text
TimerText = trtl.Turtle()
TimerText.speed(0)
TimerText.hideturtle()
TimerText.penup()
TimerText.goto(160,227)
TimerText.color("White")
TimerText.write(timer, font=Font)




### Create Game Over Screen
screen.addshape("gameOver.gif")
GameOverText = trtl.Turtle()
GameOverText.speed(0)
GameOverText.penup()
GameOverText.hideturtle()
GameOverText.shape("gameOver.gif")
GameOverText.goto(-30,-20)

### Player Movement Functions ###
#Moves The Player Up
def Up():
    Player.seth(90)
    xCor, yCor = Player.position()
    if CheckOutBounds(10, "Up", xCor, yCor):
        Player.forward(playerMovementSpeed)
        CheckCollision()
    
#Moves The Player Right
def Right():
    xCor, yCor = Player.position()
    Player.seth(0)
    if CheckOutBounds(10, "Right", xCor, yCor):
        Player.forward(playerMovementSpeed)
        CheckCollision()

#Moves The Player Left
def Left():
    xCor, yCor = Player.position()
    Player.seth(180)
    if CheckOutBounds(10, "Left", xCor, yCor):
        Player.forward(playerMovementSpeed)
        CheckCollision()

#Moves The Player Down
def Down():
    Player.seth(270)
    xCor, yCor = Player.position()
    if CheckOutBounds(10, "Down", xCor, yCor):
        Player.forward(playerMovementSpeed)
        CheckCollision()

### Checks If Enemies And/Or The Player Is Out Of Bounds ###
def CheckOutBounds(speed, direction, xCor, yCor):
    if direction == "Up" and yCor + speed < 330:
        return True 
    elif direction == "Down" and yCor - speed > -290:
        return True
    elif direction == "Right" and xCor + speed < 300:
        return True
    elif direction == "Left" and xCor - speed > -320:
        return True

### Key Presses For Player Movement ###
#Up Movements
screen.onkey(Up, "Up")
screen.onkey(Up, "w")

#Left Movements
screen.onkey(Left, "Left")
screen.onkey(Left, "a")

#Right Movements
screen.onkey(Right, "Right")
screen.onkey(Right, "d")

#Down Movements
screen.onkey(Down, "Down")
screen.onkey(Down, "s")

#Looks for key presses
screen.listen() 

### Enemy Movements [Random] ###
'''Next add: carrot moves toward potato after 30 seconds'''
def CarrotMovement():
    for i in range(len(carrots)):
        direction = rnd.randint(0,3) * 90
        carrots[i].seth(direction)
        if direction == 0:
            direction = "Right"
        elif direction == 90:
            direction = "Up"
        elif direction == 180:
            direction = "Left"
        else:
            direction = "Down"
        carX, carY = carrots[i].position()
        #Checks if the move will bring the carrot out of bounds
        if CheckOutBounds(17, direction, carX, carY):
            carrots[i].forward(CarrotMovementSpeed)
        CheckCollision()
    #Checks if the game is over
    #If the game is over, the carrot timer will stop
    if not gameOver:
        screen.ontimer(CarrotMovement, 25)

### Check For Collisions ###
def CheckCollision():
    playerX, playerY = Player.position()
    for i in range(len(carrots)):
        carrotX, carrotY = carrots[i].position()
        if (playerX - carrotX < 45 and playerX - carrotX > -45) and (playerY - carrotY < 70 and playerY - carrotY > -70):
            carrots[i].forward(300)
            Damaged()

### Player Damaged ###
def Damaged():
    global lives
    if lives > 0:
        lives = lives - 1
        hearts[lives].shape("damaged.gif")
        if lives == 0:
            GameOver()

### Game Over Sequence ###
def GameOver():
    global gameOver
    gameOver = True
    for i in range(len(hearts)):
        hearts[i].hideturtle()
    for i in range(len(carrots)):
        carrots[i].hideturtle()
    Player.hideturtle()
    TimerIcon.hideturtle()
    GameOverText.showturtle()
    TimerText.goto(0,-300)
    TimerText.color("Black")
    TimerText.clear()
    TimerText.write("You Survived For\n" + str(timer) + " Seconds", font=Font, align="Center")

### On Screen Timer ###
def Timer():
    global timer
    if not gameOver: #Checks to make sure the game is still going
        timer += 1
        TimerText.clear()
        TimerText.write(timer, font=Font)
        screen.ontimer(Timer, 1000)
        
### Timers ###
#Carrot Movement Timer
screen.ontimer(CarrotMovement, 25)


#On Screen Timer
screen.ontimer(Timer, 1000)

### End of Main Loop ###
trtl.Screen().mainloop()