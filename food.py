from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.speed('fastest')
        self.penup()
        self.shapesize(0.5, 0.5, 0.5)
        self.change_place(580, 320)

    def dot_pos(self):
        return self.pos()

    def change_place(self, max_x, max_y):
        self.goto(random.randint(-max_x, max_x), random.randint(-max_y, max_y))


class BigFood(Food):
    pass
