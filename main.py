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
scoreboard = Scoreboard()


car_manager = CarManager()

screen.onkeyrelease(fun=player.move_forward, key='Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() > 290:
        player.starting()
        scoreboard.update_score()
        car_manager.speeding()
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            scoreboard.lost()
            game_is_on = False


screen.exitonclick()