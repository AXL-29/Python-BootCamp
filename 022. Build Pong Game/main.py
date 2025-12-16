import time
from turtle import Screen, Turtle

screen = Screen()
paddle = Turtle("square")

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle.color("white")
paddle.penup()
paddle.turtlesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)

def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")

while True:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
