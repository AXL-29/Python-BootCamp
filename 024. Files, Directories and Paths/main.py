import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL_LIMIT = 280

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    if (snake.head.xcor() > WALL_LIMIT + 10 or
        snake.head.xcor() < -WALL_LIMIT - 10 or
        snake.head.ycor() > WALL_LIMIT + 10 or
        snake.head.ycor() < -WALL_LIMIT - 10 ):

        is_game_on = False
        scoreboard.game_over()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_segment()
        scoreboard.increase_score()

    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
