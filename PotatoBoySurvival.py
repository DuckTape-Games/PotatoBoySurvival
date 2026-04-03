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

## Pixel Numbers ##
numbers = []
for i in range(10):
    numbers.append("PixelNumbers/" + str(i) + ".gif")
    screen.addshape(numbers[i])
#Create turtles for ones, tens, and hundreds place
digits = []
for i in range(3):
    digits.append(trtl.Turtle())
    digits[i].hideturtle()
    digits[i].speed(0)
    digits[i].shape(numbers[0])
    digits[i].penup()
    if i == 0:
        digits[i].goto(260, 265)
    elif i == 1:
        digits[i].goto(220, 265)
    else:
        digits[i].goto(180, 265)
    digits[i].showturtle()

### Create Game Over Screen
screen.addshape("gameOver.gif")
GameOverText = trtl.Turtle()
GameOverText.speed(0)
GameOverText.penup()
GameOverText.hideturtle()
GameOverText.shape("gameOver.gif")
GameOverText.goto(-35,30)

### Create Survival Time Text ###
screen.addshape("survivalTime.gif")
SurvivalTimeText = trtl.Turtle()
SurvivalTimeText.speed(0)
SurvivalTimeText.penup()
SurvivalTimeText.hideturtle()
SurvivalTimeText.shape("survivalTime.gif")
SurvivalTimeText.goto(-5,-190)

### New Game Button ###
screen.addshape("newGame.gif")
screen.addshape("newGamePressed.gif") #changes to this when New Game is pressed
NewGame = trtl.Turtle()
NewGame.speed(0)
NewGame.penup()
NewGame.hideturtle()
NewGame.shape("newGame.gif")
NewGame.goto(0,-280)

### Player Movement Functions ###
#Moves The Player Up
def Up():
    Player.seth(90)
    xCor, yCor = Player.position()
    if CheckOutBounds(playerMovementSpeed, "Up", xCor, yCor):
        Player.forward(playerMovementSpeed)
        CheckCollision()
    
#Moves The Player Right
def Right():
    xCor, yCor = Player.position()
    Player.seth(0)
    if CheckOutBounds(playerMovementSpeed, "Right", xCor, yCor):
        Player.forward(playerMovementSpeed)
        CheckCollision()

#Moves The Player Left
def Left():
    xCor, yCor = Player.position()
    Player.seth(180)
    if CheckOutBounds(playerMovementSpeed, "Left", xCor, yCor):
        Player.forward(playerMovementSpeed)
        CheckCollision()

#Moves The Player Down
def Down():
    Player.seth(270)
    xCor, yCor = Player.position()
    if CheckOutBounds(playerMovementSpeed, "Down", xCor, yCor):
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
    return False

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
def CarrotMovement():
    global CarrotMovementSpeed
    for i in range(len(carrots)):
        if timer < 10:
            RandomMovement(carrots[i])
        else:
           if CarrotMovementSpeed != 7 and timer >= 10:
               CarrotMovementSpeed = 7
           FollowPlayer(carrots[i])
        CheckCollision()
    #Checks if the game is over
    #If the game is over, the carrot timer will stop
    if not gameOver:
        screen.ontimer(CarrotMovement, 25) #restart carrot movement loop

### Random Movement
def RandomMovement(carrot):
    direction = rnd.randint(0,3) * 90
    carrot.seth(direction)
    if direction == 0:
        direction = "Right"
    elif direction == 90:
        direction = "Up"
    elif direction == 180:
        direction = "Left"
    else:
        direction = "Down"
    carX, carY = carrot.position()
    #Checks if the move will bring the carrot out of bounds
    if CheckOutBounds(CarrotMovementSpeed, direction, carX, carY):
        carrot.forward(CarrotMovementSpeed)

### Move Towards Player AI ###
def FollowPlayer(carrot):
    if Player.xcor() > carrot.xcor():
        carrot.seth(0)
        carrot.forward(CarrotMovementSpeed)
    else:
        carrot.seth(180)
        carrot.forward(CarrotMovementSpeed)
    if Player.ycor() > carrot.ycor():
        carrot.seth(90)
        carrot.forward(CarrotMovementSpeed)
    else:
        carrot.seth(270)
        carrot.forward(CarrotMovementSpeed)

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
    SurvivalTimeText.showturtle()
    digits[0].goto(-125,-198)
    digits[1].goto(-165,-198)
    digits[2].goto(-205,-198)
    NewGame.showturtle()

### On Screen Timer ###
def Timer():
    global timer
    if not gameOver: #Checks to make sure the game is still going
        timer += 1
        timerMath = timer
        if timer <= 999:
            for i in range(len(digits)):
                digits[i].shape(numbers[timerMath % 10])
                timerMath = int(timerMath / 10)
        screen.ontimer(Timer, 1000) #restart timer loop

### Resets the game to default state ###
def StartNewGame(x,y):
    #Global Variables for this method
    global gameOver
    global lives
    global timer
    #Change NewGame to the pressed color
    NewGame.shape("newGamePressed.gif")
    #Hide objects shown during end screen
    NewGame.hideturtle()
    NewGame.shape("newGame.gif")
    GameOverText.hideturtle()
    SurvivalTimeText.hideturtle()
    #Place hearts back on the screen
    for i in range(len(hearts)):
        hearts[i].showturtle()
        hearts[i].shape("heart.gif")
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
    #Add the player back to the screen
    Player.showturtle() 
    Player.goto(100,-100)
    #Add the timer and clock back to the screen
    TimerIcon.showturtle()  
    timer = 0
    for i in range(len(digits)):
        digits[i].shape("PixelNumbers/0.gif")
    digits[0].goto(260, 265)
    digits[1].goto(220, 265)
    digits[2].goto(180, 265)
    #Restart carrot movement and clock timer
    screen.ontimer(Timer, 1000)
    screen.ontimer(CarrotMovement, 25)
    #Disable gameOver variable
    gameOver = False

### Button press for a new game ###
NewGame.onclick(StartNewGame)
        
### Timers ###
#Carrot Movement Timer
screen.ontimer(CarrotMovement, 25)

#On Screen Timer
screen.ontimer(Timer, 1000)

### End of Main Loop ###
trtl.Screen().mainloop()