import time
from turtle import Screen
from paddle import Paddle
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

# --- Paddle collision helper ---
def check_paddle_collision(ball, paddle, side="right"):
    if side == "right":
        if ball.xcor() > 320 and ball.xcor() < 350:
            if abs(ball.ycor() - paddle.ycor()) < 50:
                ball.bounce_x()
    else:  # left paddle
        if ball.xcor() < -320 and ball.xcor() > -350:
            if abs(ball.ycor() - paddle.ycor()) < 50:
                ball.bounce_x()

# --- Main game loop ---
while True:
    screen.update()
    time.sleep(0.03)

    # Move paddles
    left_paddle.move()
    right_paddle.move()

    # Move ball
    ball.move()

    # Wall collision
    if abs(ball.ycor()) > 290:
        ball.bounce_y()

    # Paddle collisions
    check_paddle_collision(ball, right_paddle, "right")
    check_paddle_collision(ball, left_paddle, "left")

    # Ball reset if passed paddles
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.reset_position()
