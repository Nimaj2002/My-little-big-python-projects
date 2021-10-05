from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score_board = Turtle()
        self.score_board.penup()
        self.score_board.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.score_board.clear()
        self.score_board.goto(-280, 250)
        self.score_board.write(f"score: {self.score}", font=FONT)

    def get_point(self):
        self.score += 1
        self.update()

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(-100, 0)
        game_over.write("Game Over!", font=FONT)
