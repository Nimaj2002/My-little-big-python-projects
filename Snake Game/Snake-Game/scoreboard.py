from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, 310)
        self.write(arg=f"score\t{self.score}", move=False, align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", move=False, align="center", font=("Courier", 40, "bold"))