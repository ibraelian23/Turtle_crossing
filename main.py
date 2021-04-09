import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    for new_car in car.cars:
        car.move_car(new_car)
        if(player.distance(new_car) < 20):
            score.game_over()
            game_is_on = False
    if(player.crossed_finish_line()):
        score.level_up()
        player.reset_player()
        car.car_accelerate()

screen.exitonclick()