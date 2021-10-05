from turtle import Turtle


class ScreenIndicator(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-380, 290)
        self.pendown()
        self.goto(380, 290)
        self.goto(380, -290)
        self.goto(-380, -290)
        self.goto(-380, 290)
