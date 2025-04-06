from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 350)
        self.refresh()

    def refresh(self):
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
