import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

color_list = [(155, 73, 46), (235, 238, 244), (52, 92, 123),
              (224, 201, 135), (171, 153, 40), (138, 31, 21),
              (132, 162, 185), (200, 91, 71), (48, 122, 87),
              (14, 99, 73), (95, 73, 75), (146, 178, 147),
              (72, 47, 38), (163, 142, 158), (234, 175, 165),
              (55, 46, 50), (184, 206, 172), (19, 85, 90),
              (144, 21, 24), (41, 62, 74), (82, 145, 128),
              (181, 87, 89), (41, 66, 90), (13, 71, 68),
              (213, 178, 183), (179, 191, 207)]

tim.setheading(220)
tim.penup()
tim.forward(300)
tim.setheading(0)


def forward_0():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


def turn_on_right():
    tim.setheading(90)
    tim.forward(50)
    tim.dot(20, random.choice(color_list))
    tim.setheading(180)


def turn_on_left():
    tim.setheading(90)
    tim.forward(50)
    tim.dot(20, random.choice(color_list))
    tim.setheading(0)


for _ in range(10):
    forward_0()
    tim.dot(20, random.choice(color_list))
    turn_on_right()
    forward_0()
    tim.dot(20, random.choice(color_list))
    turn_on_left()

screen = t.Screen()
screen.exitonclick()



