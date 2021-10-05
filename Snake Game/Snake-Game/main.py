from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from screenindicator import ScreenIndicator
import time

# Screen Properties
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# -----
screen_indicator = ScreenIndicator()

# creating all objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# connecting keys to funcs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.eating()
        food.refresh()
        scoreboard.score += 1
        scoreboard.show_score()

    # detect collision with wall
    if snake.head.xcor() >= 330 or snake.head.xcor() <= -330 or snake.head.ycor() >= 300 or snake.head.ycor() <= -330:
        game_is_on = False

    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False


if not game_is_on:
    scoreboard.game_over()

screen.exitonclick()
