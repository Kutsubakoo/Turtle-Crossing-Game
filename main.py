import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from line import Line

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
score = Scoreboard()
line = Line()

player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()

    car.generate_car()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            player.reset_position()
            car.game_over()
            score.reset_score()

    if player.ycor() == 270:
        score.update_level()
        player.reset_position()
        car.faster()






screen.exitonclick()