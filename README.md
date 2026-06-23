# Potato Boy Survival

An endless arcade survival game where Potato Boy must avoid three hostile Carrot Men for as long as possible.

The project began as a Java final project for AP Computer Science A and was later rebuilt in Python using Turtle graphics. The Python version became the first released game from DuckTape Games.

## Features

* Endless survival-based gameplay
* Three animated Carrot Man enemies
* Three-life health system with heart indicators
* Survival timer displayed with custom pixel-number graphics
* Random enemy movement during the opening 10 seconds
* Player-tracking enemy movement after 10 seconds
* Animated Potato Boy and Carrot Man sprites
* Independent animation states for each enemy
* Collision sound effects
* Looping gameplay and game-over music
* Game-over screen showing the final survival time
* New Game button for restarting without closing the application
* WASD and arrow-key movement controls
* Fixed 700 x 700 game window

## Project Background

Potato Boy Survival was originally created in Java as a final project for AP Computer Science A.

It was later rebuilt in Python with Turtle and Pygame Mixer, becoming the first game released by DuckTape Games. The Python version expands the original concept with animated sprites, custom visual assets, sound effects, music, a visible life system, and a restartable game-over screen.

## Gameplay

The game begins immediately after launching.

Potato Boy starts with three lives while three Carrot Men move around the arena. During the first 10 seconds, the enemies move in random directions at a higher movement speed. After that, they slow down and begin moving directly toward Potato Boy.

Each collision removes one life and sends the Carrot Man away from the player. The game ends when all three lives are lost.

The goal is to survive for as many seconds as possible.

## Controls

| Action | Keys |
| --- | --- |
| Move up | `W` or Up Arrow |
| Move down | `S` or Down Arrow |
| Move left | `A` or Left Arrow |
| Move right | `D` or Right Arrow |
| Start a new game | Click **New Game** after losing |

## Enemy Behavior

The Carrot Men use two movement systems:

1. **Random movement:** For the first 10 seconds, each enemy repeatedly chooses a random cardinal direction.
2. **Player tracking:** After 10 seconds, each enemy compares its position with Potato Boy and moves horizontally and vertically toward him.

Each Carrot Man has its own animation state, allowing all three enemies to animate independently while moving.

## Lives and Collisions

Potato Boy begins each game with three lives.

When a Carrot Man collides with Potato Boy:

* One life is removed.
* One heart changes to its damaged state.
* A collision sound plays.
* The enemy is moved 300 pixels away in a valid direction.
* The game continues until no lives remain.

When all lives are lost, the active game objects are hidden. The game-over screen then displays the final survival time and a New Game button.

## Scoring

The score is the number of seconds Potato Boy survives.

The timer increases once per second and uses three custom pixel-number sprites. After the game ends, the final timer value is displayed as the survival time for that attempt.

## Requirements

* Python 3
* Pygame
* Tkinter and Turtle support, normally included with standard Python installations
* Windows is recommended because the game loads a Windows `.ico` file through Tkinter

Install Pygame with:

```bash
pip install pygame
```

Some Linux installations require Tkinter to be installed separately. The application icon line may also need to be changed or removed on non-Windows systems.

## Running From Source

Clone or download the repository, open the project directory, and run:

```bash
python PotatoBoySurvival.py
```

Run the command from the project directory. The game loads images and audio through relative file paths, so the asset files and `PixelNumbers` folder must remain beside the Python script.

## Building a Windows EXE

The game can be packaged with Auto Py to Exe or PyInstaller.

Because the current code uses direct relative asset paths, a **One Directory** build is recommended. All image and audio files must remain beside the executable, and the `PixelNumbers` folder must retain its name and structure.

Recommended Auto Py to Exe settings:

* Script Location: `PotatoBoySurvival.py`
* One Directory
* Window Based
* Icon: `potatoBoy.ico`
* Additional Folder: `PixelNumbers`
* Add every root-level `.gif` and `.wav` asset as an additional file

The application expects files such as these to remain available relative to the executable:

```text
bg.gif
potatoBoy.ico
musicLoop.wav
gameOverMusicLoop.wav
hitSound.wav
PixelNumbers\0.gif
```

A one-file build requires updating the project to resolve bundled resource paths before the assets will load reliably.

## Project Structure

```text
PotatoBoySurvival/
├── PixelNumbers/
│   ├── 0.gif
│   ├── 1.gif
│   ├── 2.gif
│   ├── 3.gif
│   ├── 4.gif
│   ├── 5.gif
│   ├── 6.gif
│   ├── 7.gif
│   ├── 8.gif
│   └── 9.gif
├── PotatoBoySurvival.py
├── Patch Notes.txt
├── bg.gif
├── carrotFrame1.gif
├── carrotFrame2.gif
├── carrotMan.gif
├── damaged.gif
├── gameOver.gif
├── gameOverMusicLoop.wav
├── heart.gif
├── hitSound.wav
├── musicLoop.wav
├── newGame.gif
├── newGamePressed.gif
├── potatoBoy.gif
├── potatoBoy.ico
├── potatoFrame1.gif
├── potatoFrame2.gif
├── survivalTime.gif
└── timer.gif
```

## How It Works

1. The game creates a fixed Turtle window and loads the visual assets.
2. Pygame Mixer starts the looping background music.
3. Potato Boy is controlled through keyboard events.
4. Enemy movement updates every 50 milliseconds.
5. The survival timer increases once per second.
6. The Carrot Men move randomly until the timer reaches 10 seconds.
7. The enemies then begin following Potato Boy.
8. Collision checks compare the player's position with each enemy.
9. Losing all three lives starts the game-over sequence.
10. Clicking **New Game** resets the characters, lives, timer, music, and enemy behavior.

## Technical Details

* Turtle handles rendering, keyboard input, mouse input, animation, and timed callbacks.
* Pygame Mixer handles background music and collision audio.
* The player moves 15 pixels per key press.
* The enemies use a movement value of 17 during the opening random phase.
* Their movement value changes to 5 when player tracking begins.
* Enemy tracking uses separate horizontal and vertical position comparisons.
* The timer uses three custom pixel digits.
* Each enemy maintains an independent animation state.
* The New Game button resets the existing game objects rather than reopening the program.

## Notes

* The displayed survival time supports values from `000` through `999`.
* The game does not save a high score between sessions.
* There is no pause system.
* The game starts immediately without a separate title screen.
* Root-level assets must remain in the same working directory as the script.
* `potatoBoy.gif` and `carrotMan.gif` appear to be earlier static versions of the animated character sprites.

## Possible Future Improvements

Ideas documented in the source code include:

* Additional directional animation frames
* Pepper Kid power-ups that temporarily increase movement speed
* Broccoli Guy power-ups that restore a life when the player is down to one heart

## Current Status

The game is complete and playable as an endless survival challenge.

The latest included patch notes document:

* Player and enemy animation
* Independent enemy animation states
* Smoother enemy movement timing
* Improved visual feedback
* Minor timing stability fixes

## Credits

**Development**

Chris Herriman Jr.

**Publisher**

DuckTape Games

**Music**

Gameplay music by EEE3333E on Freesound. The game-over track is a modified version of the gameplay loop.

**Sound Effects**

Hit sound by Sadiquecat on Freesound.
