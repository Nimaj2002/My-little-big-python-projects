import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(fun=player.move_up, key="Up")

car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    if player.reached_top():
        score_board.get_point()
        car_manager.increase_speed()

    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
