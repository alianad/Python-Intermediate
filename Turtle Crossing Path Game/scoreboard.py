from turtle import Turtle

FONT = ("Courier", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.current_level = 1
        self.update_level()

    def level_up(self):
        self.current_level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level : {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
