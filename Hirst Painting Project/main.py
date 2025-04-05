# import colorgram
import turtle
import random

# -------- extract colors from image ----------
# rgb_colors = []
# colors = colorgram.extract("img.jpg", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

colour_list = [(216, 165, 84), (240, 242, 247), (242, 237, 228), (81, 102, 149), (245, 226, 240), (112, 160, 204), (68, 126, 96), (110, 173, 134), (131, 21, 60), (236, 246, 241), (158, 48, 84), (218, 203, 126), (159, 159, 50), (203, 118, 162), (125, 117, 167), (190, 70, 41), (34, 37, 81), (205, 100, 55), (74, 139, 178), (197, 83, 103)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")

tim.hideturtle()
tim.penup()
tim.setheading(220)
tim.forward(380)
tim.setheading(0)

for width in range(10):
    for dot in range(10):
        tim.dot(15, random.choice(colour_list))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
