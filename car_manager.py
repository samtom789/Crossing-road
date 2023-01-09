from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.all_cars = []


    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            self.car = Turtle()
            self.car.penup()
            self.car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            self.car.shape('square')
            self.car.goto(300, y_cor)
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(self.car)
    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)



