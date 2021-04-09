from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed=5

    def create_cars(self):
        if(random.randint(1, 6) == 1):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(x=300, y=random.randint(-250, 250))
            self.cars.append(car)

    def move_car(self, new_car):
        new_car.back(self.move_speed)

    def car_accelerate(self):
        self.move_speed += 10
