from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, y_cor)

        # Movement flags
        self.move_up_flag = False
        self.move_down_flag = False
        self.speed_step = 20

    # Key press/release methods
    def start_up(self):
        self.move_up_flag = True

    def stop_up(self):
        self.move_up_flag = False

    def start_down(self):
        self.move_down_flag = True

    def stop_down(self):
        self.move_down_flag = False

    # Called every frame
    def move(self):
        new_y = self.ycor()
        if self.move_up_flag:
            new_y += self.speed_step
        if self.move_down_flag:
            new_y -= self.speed_step

        # Clamp paddle to screen
        if new_y > 250:
            new_y = 250
        if new_y < -250:
            new_y = -250

        self.sety(new_y)
