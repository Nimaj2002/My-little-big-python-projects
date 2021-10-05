import turtle as t
from random import randint

ted = t.Turtle()
ted.speed("fastest")
t.colormode(255)
for x in range(100):
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    ted.color(R, G, B)
    ted.setheading(10*x)
    ted.circle(100)

screen = t.Screen()
screen.exitonclick()