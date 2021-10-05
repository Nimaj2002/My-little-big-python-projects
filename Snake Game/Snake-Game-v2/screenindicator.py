from turtle import Turtle


class ScreenIndicator(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-330, 290)
        self.pendown()
        self.goto(330, 290)
        self.goto(330, -330)
        self.goto(-330, -330)
        self.goto(-330, 290)