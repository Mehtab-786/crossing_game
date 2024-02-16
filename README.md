# crossing_game
# Turtle Crossing Game

![Turtle Crossing Game](images/turtle_crossing_game.png)

## Introduction

Welcome to Turtle Crossing Game, a simple yet engaging turtle-themed game built using the Turtle module in Python. The objective of the game is to help the turtle cross the road while avoiding oncoming traffic.

## How to Play

1. **Controls:**
    - Move the turtle forward: Press the "Up" arrow key.

2. **Gameplay:**
    - The turtle starts at the bottom of the screen and must cross the road to reach the top.
    - Be cautious of moving cars! If the turtle collides with a car, the game ends.

3. **Scoring:**
    - Successfully crossing the road earns you points.
    - The level increases each time you successfully cross the road.

## Game Components

### Player
- The player is represented by a turtle character.
- Move the player forward to navigate across the road.

### Car Manager
- Manages the creation, movement, and speeding of cars.
- Cars appear randomly on the road and move from right to left.
- The speed of cars increases as the game progresses.

### Scoreboard
- Displays the current level.
- Updates the level when the player successfully crosses the road.
- Announces "You Lost" when the player collides with a car.

## Getting Started

1. Ensure you have Python installed on your machine.
2. Run the `turtle_crossing_game.py` file using a Python interpreter.

```bash
python turtle_crossing_game.py
```

3. Use the "Up" arrow key to move the turtle forward and navigate through the traffic.

## Dependencies
- Python 3.x
- Turtle module (built-in)
- Random module (built-in)

## Customization
- Feel free to customize the game by modifying the constants in the code, such as `COLORS`, `STARTING_MOVE_DISTANCE`, and `MOVE_INCREMENT`.

## Acknowledgments
- This game was created as a programming exercise and is inspired by classic arcade-style games.

Have fun playing Turtle Crossing Game! 🐢🚗
