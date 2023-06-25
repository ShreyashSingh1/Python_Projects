from turtle import Turtle


class LineMaker(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, -300)
        self.setheading(90)
        self.forward(600)
