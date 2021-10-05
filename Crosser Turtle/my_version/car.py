from turtle import Turtle
from random import randint

color_list = ["red", "blue", "orange", "yellow", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(color_list[randint(0, 4)])
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300, randint(-280, 280))






