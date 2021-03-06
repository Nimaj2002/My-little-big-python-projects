from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.75)
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-255, 255)
        random_y = random.randrange(-255, 255)
        self.goto(random_x, random_y)


