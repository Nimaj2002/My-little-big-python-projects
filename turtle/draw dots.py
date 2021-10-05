from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)


def change_color():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    return (R, G, B)


def go_right(user_turtle, how_far):
    # user_turtle.pendown()
    # user_turtle.forward(1)
    user_turtle.dot(20, change_color())
    for x in range(how_far):

        user_turtle.forward(100)
        # user_turtle.pendown()
        # user_turtle.forward(1)
        user_turtle.dot(20, change_color())


def go_left(user_turtle, how_far):
    # change_color(user_turtle)
    # user_turtle.pendown()
    # user_turtle.forward(1)
    user_turtle.dot(20, change_color())
    for x in range(how_far):
        # change_color(user_turtle)
        # user_turtle.penup()
        user_turtle.forward(100)
        # user_turtle.pendown()
        # user_turtle.forward(1)
        user_turtle.dot(20, change_color())


def turn_right(user_turtle):
    # user_turtle.pendown()
    user_turtle.right(90)
    # user_turtle.forward(1)
    # user_turtle.penup()
    user_turtle.forward(100)
    user_turtle.dot(20, change_color())
    user_turtle.right(90)


def turn_left(user_turtle):
    # user_turtle.pendown()
    user_turtle.left(90)
    # user_turtle.forward(1)
    # user_turtle.penup()
    user_turtle.forward(100)
    user_turtle.dot(20, change_color())
    user_turtle.left(90)


my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.color("white")
my_turtle.speed("fastest")
my_turtle.width(20)
my_turtle.penup()
my_turtle.goto(-350, 300)

for x in range(2):
    go_right(my_turtle, 5)
    turn_right(my_turtle)
    go_left(my_turtle,5)
    turn_left(my_turtle)
go_right(my_turtle, 5)
my_turtle.hideturtle()
screen = Screen()
screen.exitonclick()
