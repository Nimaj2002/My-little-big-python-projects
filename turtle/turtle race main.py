from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Your bet", prompt="Which turtle do you think will win? Enter color:\t")

is_game_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -75
for turtle_index in range(0, 6):
    racer_turtle = Turtle(shape="turtle")
    racer_turtle.color(colors[turtle_index])
    racer_turtle.penup()
    racer_turtle.goto(-230, y)
    all_turtles.append(racer_turtle)
    y += 30

if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_game_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've Won! The {winner_color} turtle is winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is winner!")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
