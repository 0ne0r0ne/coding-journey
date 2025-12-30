import turtle
import pandas

data = pandas.read_csv("50_states.csv")

data['state_lower'] = data.state.str.lower()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None or answer_state.lower() == "exit":
        missing_states = [state for state in data.state if state not in guessed_states]
        missing_df = pandas.DataFrame(missing_states)
        missing_df.to_csv("states_to_learn.csv")
        break


    answer_lower = answer_state.lower()
    matching = data[data.state_lower == answer_lower]


    if not matching.empty and answer_lower not in [s.lower() for s in guessed_states]:

        state_data = matching.iloc[0]

        guessed_states.append(state_data.state)


        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(state_data.state, align="center")

screen.mainloop()