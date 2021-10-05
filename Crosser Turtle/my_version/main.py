from turtle import Screen
from our_turtle import RunnerTurtle
from car import Car
import time
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightgray")
screen.tracer(0)
screen.listen()

runner_turtle = RunnerTurtle()
screen.onkeypress(fun=runner_turtle.go, key="Up")
cars_list = []
game_is_on = True

while game_is_on:
    time.sleep(0.5)
    screen.update()
    car = Car()
    cars_list.append(car)
    for car in cars_list:
        car.forward(10)

screen.exitonclick()
