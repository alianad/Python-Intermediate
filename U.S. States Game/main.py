import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(800, 600)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        guessed_states.append(answer)
        data_state = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(data_state.x.item(), data_state.y.item())
        t.write(arg=answer)
