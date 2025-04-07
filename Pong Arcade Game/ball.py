from turtle import Turtle

class Ball(Turtle):

    # TODO 3: Create the ball and make it move
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_move = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1
        self.speed_move *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.speed_move *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speed_move = 0.1
        self.bounce_x()
