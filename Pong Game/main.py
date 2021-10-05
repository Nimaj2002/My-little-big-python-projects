from turtle import Screen
from paddle import Paddle
from ball import Ball
from screenindicator import ScreenIndicator
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

screen_indicator = ScreenIndicator()
# Creating paddles
right_paddle = Paddle((350, 0))
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

left_paddle = Paddle((-350, 0))
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_in_on = True
ball = Ball()
score_board = Scoreboard()

sleep_time = 0.1
while game_in_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # collision with up and down walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # collision with paddles
    if ball.xcor() > 330 and ball.distance(right_paddle) < 50 or ball.xcor() < -330 and ball.distance(left_paddle) < 50:
        sleep_time -= 0.01
        ball.bounce_x()

    # collision with right and left
    if ball.xcor() > 370:
        score_board.l_point()
        sleep_time *= 0.9
        ball.reset_position()

    if ball.xcor() < -370:
        score_board.r_point()
        sleep_time *= 0.9
        ball.reset_position()


screen.exitonclick()
