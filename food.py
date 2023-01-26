from turtle import Turtle
import random
RANGE = 280
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-RANGE, RANGE)
        random_y = random.randint(-RANGE, RANGE)
        self.goto(random_x, random_y)