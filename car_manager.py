from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_no = random.randint(1,6)
        if random_no == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300,random_y)
            new_car.setheading(180)
            self.all_car.append(new_car)


    def move_car(self):
        for car in self.all_car:
            car.forward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT