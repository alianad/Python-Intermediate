from turtle import *
from random import *

is_race_on = False

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? (red / orange / pink / blue / purple / green) \nEnter the color : ")

colors = ["red", "orange", "pink", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
