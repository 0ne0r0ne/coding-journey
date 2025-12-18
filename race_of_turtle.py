from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput("Make your bet", "Which turtle will the race?\nEnter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -120
for turtle_index in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.color(colors[turtle_index])
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(-240, y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You won!\nThe {winning_color} is the winner!")
            else:
                print(f"You've lose!\nThe {winning_color} is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.mainloop()
