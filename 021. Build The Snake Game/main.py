from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turn off auto screen updates

# Game objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
game_is_on = True
WALL_LIMIT = 300
HEAD_RADIUS = 10  # half of head size

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Check wall collision
    if (
        snake.head.xcor() + HEAD_RADIUS > WALL_LIMIT or
        snake.head.xcor() - HEAD_RADIUS < -WALL_LIMIT or
        snake.head.ycor() + HEAD_RADIUS > WALL_LIMIT or
        snake.head.ycor() - HEAD_RADIUS < -WALL_LIMIT
    ):
        game_is_on = False
        scoreboard.game_over()

    # Check tail collision
    for segment in snake.segments[1:]:  # skip head
        if snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()

# Exit on click
screen.exitonclick()
