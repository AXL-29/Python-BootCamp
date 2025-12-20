"""
Main game loop for the Snake game.
Handles screen setup, user input, collisions, and game updates.
"""

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL_LIMIT = 280  # Boundary limit before collision with wall

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic screen updates

# Game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect wall collision
    if (
        snake.head.xcor() > WALL_LIMIT + 10 or
        snake.head.xcor() < -WALL_LIMIT - 10 or
        snake.head.ycor() > WALL_LIMIT + 10 or
        snake.head.ycor() < -WALL_LIMIT - 10
    ):
        scoreboard.reset()
        snake.reset()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_segment()
        scoreboard.increase_score()

    # Detect self-collision
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
