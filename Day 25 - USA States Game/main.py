import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")

image = r"Day 25 - USA States Game\blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

correct_answers = 0

data = pandas.read_csv(r"Day 25 - USA States Game\50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        cor_x = int(state_data.x.item()) 
        cor_y = int(state_data.y.item())
        t.goto(cor_x, cor_y)
        t.write(answer_state)

screen.exitonclick()