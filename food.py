from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.y_cor = None
        self.x_cor = None
        self.shape("circle")
        self.penup()
        self.color("green")

    def position_food(self):
        return self.pos()

    def reposition_food(self):
        self.x_cor = random.choice(range(-280, 280, 20))
        self.y_cor = random.choice(range(-280, 280, 20))
        self.goto(self.x_cor, self.y_cor)
#