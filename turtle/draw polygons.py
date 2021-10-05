from turtle import Turtle, Screen,colormode
from random import randint


def make_shape(user_turtle, number):
    x = 3
    while x <= number:
        R = randint(0,255)
        G = randint(0,255)
        B = randint(0,255)
        user_turtle.color(R,G,B)

        for y in range(x):
            user_turtle.forward(100)
            user_turtle.right(360/x)
        x += 1


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
colormode(255)
timmy_the_turtle.speed(100)
timmy_the_turtle.penup()
timmy_the_turtle.sety(300)
timmy_the_turtle.setx(-50)
timmy_the_turtle.pendown()
make_shape(timmy_the_turtle, 20)
screen = Screen()
screen.exitonclick()
