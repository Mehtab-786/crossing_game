from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car = randint(0,6)
        if random_car == 6:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(290, randint(-290, 280))
            car.color(choice(COLORS))
            self.all_cars.append(car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.speed)

    def speeding(self):
        self.speed += MOVE_INCREMENT

