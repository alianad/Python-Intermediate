from scoreboard import Score
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# TODO 1: Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.speed_move)
    ball.move()

    # TODO 4: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 5: Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # TODO 6: Detect when paddle misses
    # TODO 7: Keep score
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
