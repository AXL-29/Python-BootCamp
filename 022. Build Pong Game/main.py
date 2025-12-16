import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(x_cor=350, y_cor=0)
left_paddle = Paddle(x_cor=-350, y_cor=0)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

while True:
    screen.update()
    time.sleep(0.1)
    ball.move()

screen.exitonclick()
