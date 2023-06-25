import pandas
import turtle

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
timm = turtle.Turtle()


def get_mouse_click_cor(x, y):
    print(x, y)


turtle.onclick(get_mouse_click_cor)
"""listen for when the mouse clicks and then it's going to call our
get get_mouse_click_cor function, and it's going to pass over the X and Y coordinates of that click location.
turtle.mainloop is an alternative way of keeping our screen open"""

# print(ans_user)

s_data = pandas.read_csv("50_states.csv")
guessed_state = []


def write_state():
    s_row = s_data[s_data["state"] == ans_user]
    x = int(s_row.x.to_list()[0])
    y = int(s_row.y.to_list()[0])
    timm.penup()
    timm.hideturtle()
    timm.goto(x, y)
    timm.write(f"{ans_user}", align="center", font=('Arial', 8, 'normal'))


all_state = s_data["state"].to_list()
while len(guessed_state) < 50:
    ans_user = screen.textinput(title=f"Correct states {len(guessed_state)}/50", prompt="What's another state's name?").title()
    if ans_user == "Exit":
        miss_state = [state for state in all_state if state not in guessed_state]
        # for state in all_state:
        #     if state not in guessed_state:
        #         miss_state.append(state)
        print(miss_state)
        new_data_df = pandas.DataFrame(miss_state)
        new_data_df.to_csv("States_to_learn.csv")
        break
    # print(ans_user)
    if ans_user in all_state:
        if not ans_user in guessed_state:
            guessed_state.append(ans_user)
            write_state()

'''
pandas.series.item() does is it looks into the underlying data and it basically
just grabs the first element. and removes the unwanted things
'''
