import turtle
import pandas

game_is = True
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(-250, 250)

data_dict = {
    "States": [],
    "X": [],
    "Y": []
}

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()
for i in range(len(states)):
    c_state = states[i]
    c_x = x_cor[i]
    c_y = y_cor[i]
    data_dict["States"].append(c_state)
    data_dict["X"].append(c_x)
    data_dict["Y"].append(c_y)
scores = 0
already_guess = []
while game_is:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name").title()
    for i in range(len(states)):
        if scores == 50:
            game_is = False
        if answer_state == states[i]:
            if answer_state in already_guess:
                scores -= 1
            scores += 1
            already_guess.append(states[i])
            n = turtle.Turtle()
            n.hideturtle()
            n.penup()
            n.goto(x_cor[i], y_cor[i])
            n.write(arg=f"{states[i]}",move=False, align="center")
            score.clear()
            score.write(arg=f"Score: {scores}/50", move=False, align="center")



screen.exitonclick()