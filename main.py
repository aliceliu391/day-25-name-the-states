import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


def show_state(state_name, x_coor, y_coor):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.color("black")
    text.goto(x_coor, y_coor)
    text.write(state_name, align="center", font=("Courier", 12, "bold"))


info = pandas.read_csv("50_states.csv")
states_guessed = []
all_states = info.state.to_list()

still_playing = True
while len(states_guessed) < 50 and still_playing:
    answer_state = (turtle.textinput(f"{len(states_guessed)}/50 states guessed.", "What's another state name?").title().
                    strip())
    if answer_state == "Exit":
        still_playing = False
    if answer_state in all_states:
        state = info[info.state == answer_state]
        x = int(state.x.item())
        y = int(state.y.item())

        show_state(answer_state, x, y)
        states_guessed.append(answer_state)


missing_states = []
for state in all_states:
    if state not in states_guessed:
        missing_states.append(state)

    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
