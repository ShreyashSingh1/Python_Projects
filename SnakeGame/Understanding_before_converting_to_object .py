# """When problem is complex break it down into parts
# here we are dividing this game into 7 parts
# 1.Create a snake body
# 2.Move the snake
# 3.Control the snake using keyboard
# 4.Detect the collision with food
# 5.Create the score
# 6.Detect collision with wall
# 7.Detect collision with tail
# """
# from turtle import Turtle, Screen
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title("Snake Game")
# # Turn turtle animation on/off and set delay for update drawings
# # Can be used to accelerate the drawing of complex graphics.
# screen.tracer(0)
# # 0 == off
# segments = []
#
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# """Snake creation"""
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.penup()
#     new_segment.color("White")
#     new_segment.goto(position)
#     segments.append(new_segment)
#
# game_is_on = True
# while game_is_on:
#     """we can use the update method to tell our program when to refresh and redraw"""
#     # maybe move each of our segments and then tell the screen to update again
#     # to show the user the new result.
#     # And then each time we make the changes we want to happen
#     # and then call that update method to tell the screen
#     # Perform a TurtleScreen update. To be used when tracer is turned off.
#     screen.update()
#     # Python sleep() call to simulate a delay in your program.
#     time.sleep(0.1)
#     # Here we have decided how the segment of snake will move as in last segment will follow the 2nd last segment so on...
#     for seg_no in range(len(segments)-1, 0, -1):
#         new_x = segments[seg_no-1].xcor()
#         new_y = segments[seg_no-1].ycor()
#         segments[seg_no].goto(new_x, new_y)
#     segments[0].forward(20)
#
# screen.exitonclick()


# Class inheritance
class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

"""The call to super() in the initialiser is recommended, but not strictly required."""


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
