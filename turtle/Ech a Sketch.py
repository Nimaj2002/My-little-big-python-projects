from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)
my_turtle = Turtle()
my_turtle.speed("fastest")
my_turtle.shape("turtle")
my_turtle.width(5)
screen = Screen()
screen.listen()


def move_forward():
    my_turtle.pendown()
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    my_turtle.color(R, G, B)
    my_turtle.forward(10)


def move_backward():
    my_turtle.pendown()
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    my_turtle.color(R, G, B)
    my_turtle.backward(10)


def turn_clockwise():
    my_turtle.pendown()
    my_turtle.right(10)


def turn_counter_clockwise():
    my_turtle.pendown()
    my_turtle.left(10)


def clear():
    my_turtle.color("black")
    my_turtle.penup()
    my_turtle.clear()
    my_turtle.home()


def go_forward():
    my_turtle.penup()
    my_turtle.forward(10)


def go_backward():
    my_turtle.penup()
    my_turtle.backward(10)


def go_to_right():
    my_turtle.penup()
    my_turtle.right(10)


def go_to_left():
    my_turtle.penup()
    my_turtle.left(10)


def draw_circle():
    my_turtle.pendown()
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    my_turtle.color(R, G, B)
    my_turtle.circle(100)


screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=turn_clockwise, key="d")
screen.onkeypress(fun=turn_counter_clockwise, key="a")
screen.onkeypress(fun=clear, key="c")
screen.onkeypress(fun=go_forward, key="Up")
screen.onkeypress(fun=go_backward, key="Down")
screen.onkeypress(fun=go_to_right, key="Right")
screen.onkeypress(fun=go_to_left, key="Left")
screen.onkeypress(fun=draw_circle, key="g")
screen.exitonclick()
