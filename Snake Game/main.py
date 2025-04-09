from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # TODO 5: Detect collision with food
    # TODO 6: Create a scoreboard
    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # TODO 7: Detect collision with wall
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        scoreboard.reset_scoreboard()
        snake.reset()

    # TODO 8: Detect collision with tail (list slicing)
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 8:
            print(f"Collided with tail segment at {segment.position()}")
            scoreboard.reset_scoreboard()

screen.exitonclick()
