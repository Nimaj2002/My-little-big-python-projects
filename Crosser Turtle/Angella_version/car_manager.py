from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 6:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.goto(300, randint(-250, 250))
            car.color(COLORS[randint(0, 5)])
            self.cars_list.append(car)

    def move_car(self):
        for car in self.cars_list:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT

    # def collision(self):
    #     for car in self.cars_list: