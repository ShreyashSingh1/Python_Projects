from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=280)
        self.score = 0
        with open("scoretracker.txt", mode="r+") as data:
            self.hs = int(data.read()) # hs = high score

    def in_score(self):
        self.score += 1

    def display(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.hs}", align="center", font=('Arial', 12, 'normal'))

    def reset(self):
        if self.score > self.hs:
            self.hs = self.score
            with open("scoretracker.txt", mode="w") as data:
                data.write(f"{self.hs}")
        self.score = 0
        self.display()

    # def gameover(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over your score: {self.score}", align="center", font=('Arial', 12, 'normal'))


# Use to write text in our program using turtle
"""turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
Parameters
arg – object to be written to the TurtleScreen
move – True/False
align – one of the strings “left”, “center” or right”
font – a triple (fontname, font-size, font type)

Write text - the string representation of arg - at the current turtle position according to align 
(“left”, “center” or “right”) and with the given font. 
If move is true, the pen is moved to the bottom-right corner of the text. By default, move is False."""
