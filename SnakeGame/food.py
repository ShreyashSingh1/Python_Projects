from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # allows me to do is to stretch the turtle along its length and along its width.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        ran_x1 = random.randint(-280, 280)
        ran_y1 = random.randint(-280, 280)
        self.goto(ran_x1, ran_y1)
