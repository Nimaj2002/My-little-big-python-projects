import turtle
import pandas
#######################################################################################################
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_count = 50
states_answered = 0

writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()
writer_turtle.speed("fastest")
#######################################################################################################
all_csv_data = pandas.read_csv("50_states.csv")
all_states_names = all_csv_data["state"]
answered_list = []
#######################################################################################################
try:
    while states_answered <= 50:
        answer_states = screen.textinput(title=f"{states_answered}/{states_count} States Correct",
                                         prompt="What's another state's name?")
        for state in all_states_names:
            if state in answered_list:
                pass
            elif state.lower() == answer_states.lower():
                state_data = all_csv_data[all_csv_data.state == state]
                x_cor = int(state_data.x)
                y_cor = int(state_data.y)
                states_answered += 1
                writer_turtle.goto(x_cor, y_cor)
                writer_turtle.write(f"{state}", font=("Times New Roman", 10, "normal"))
                answered_list.append(state)
        if states_answered == 50:
            writer_turtle.goto(-100, 0)
            writer_turtle.write(f"You Won!!", font=("Times New Roman", 30, "normal"))

    turtle.mainloop()

except AttributeError:
    missing_state = [state for state in all_states_names if state not in answered_list]
    new_data = pandas.DataFrame(missing_state)
    new_data.to_csv("Missing_States.csv")

    exit()