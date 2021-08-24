import random
from random import randint
from turtle import Turtle

SHAPE_LIST = ["square", "turtle", "circle", "triangle"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(SHAPE_LIST))
        if self.shape() == "turtle":
            self.color("green")
        else:
            self.color("blue")
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
