import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# --- Screen setup ---
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# --- Create paddles and ball ---
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

# --- Keyboard controls ---
screen.listen()
# Right paddle
screen.onkeypress(right_paddle.start_up, "Up")
screen.onkeyrelease(right_paddle.stop_up, "Up")
screen.onkeypress(right_paddle.start_down, "Down")
screen.onkeyrelease(right_paddle.stop_down, "Down")
# Left paddle
screen.onkeypress(left_paddle.start_up, "w")
screen.onkeyrelease(left_paddle.stop_up, "w")
screen.onkeypress(left_paddle.start_down, "s")
screen.onkeyrelease(left_paddle.stop_down, "s")

# --- Main game loop ---
while True:
    screen.update()
    time.sleep(ball.move_speed)

    # Move paddles
    left_paddle.move()
    right_paddle.move()

    # Move ball
    ball.move()

    # Wall collision
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Paddle collisions
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()        

    # Ball reset if passed paddles
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    