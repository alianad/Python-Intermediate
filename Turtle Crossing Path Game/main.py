from car_manager import CarManager
from scoreboard import ScoreBoard
from player import  Player
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Path")
screen.tracer(0)

player = Player()
cars = CarManager()
level = ScoreBoard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            level.game_over()

    if player.is_at_finish_line():
        player.starting_position()
        level.level_up()
        cars.speed_up()

screen.exitonclick()
