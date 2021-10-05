from turtle import Turtle, colormode
from random import randint


def walk_and_turn(user_turtle):
    degrees = [90, 180, 270, 360]
    random_degree = degrees[randint(0, 3)]
    user_turtle.right(random_degree)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    user_turtle.color(red, green, blue)
    user_turtle.width(20)
    user_turtle.forward(50)


colormode(255)
My_turtle = Turtle()
My_turtle.shape("circle")
My_turtle.speed(300)
while True:
    walk_and_turn(My_turtle)
