import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]
# state_x = data["x"]
# state_y = data["y"]
t=turtle.Turtle()
def answer_text():
    t.write(answer_state)

def move_state():
    state_location = data[data.state == answer_state]
    t.hideturtle()
    t.penup()
    t.goto(state_location.x.item(), state_location.y.item())

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's next state's name?").title()
    guessed_states.append(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in states:
        if answer_state == state:
            move_state()
            answer_text()
    







# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)


