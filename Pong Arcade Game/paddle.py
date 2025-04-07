from turtle import Turtle

class Paddle(Turtle):

    # TODO 2: Create and move a paddle
    def __init__(self, position):
        super().__init__()
        paddle = Turtle()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=0.1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
