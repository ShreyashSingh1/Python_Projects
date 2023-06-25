"""
When problem is complex break it down into parts here we are dividing this game into 7 parts
1.Create a snake body
2.Move the snake
3.Control the snake using keyboard
4.Detect the collision with food
5.Create the score
6.Detect collision with wall
7.Detect collision with tail
"""

from turtle import Screen
from snake import Snake
import food
import scoreboard
import pyttsx3
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
# Turn turtle animation on/off and set delay for update drawings
# Can be used to accelerate the drawing of complex graphics.
screen.tracer(0)
# 0 == off

snake = Snake()
food = food.Food()
score_board = scoreboard.Scoreboard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

Shreyash = pyttsx3.init()
Shreyash.say("Welcome to Snake game")
Shreyash.runAndWait()

game_is_on = True
while game_is_on:
    '''we can use the update method to tell our program when to refresh and redraw'''
    # maybe move each of our segments and then tell the screen to update again
    # to show the user the new result.
    # And then each time we make the changes we want to happen
    # and then call that update method to tell the screen
    # Perform a TurtleScreen update. To be used when tracer is turned off.
    screen.update()
    ''' Python sleep() call to simulate a delay in your program.'''
    time.sleep(0.1)
    snake.move()
    score_board.display()
    # Detect collision with food
    """The distance method works by comparing the distance from this turtle to whatever it is that you put inside the parentheses.
     comparing this turtle against another turtle,and trying to get hold of the distance between the two turtles."""
    if snake.head.distance(food) < 15:
        # food bhi turtle hai bhai Superclass/sub class yaad kar
        food.move_food()
        snake.extend()
        #Delete the turtle’s drawings from the screen. Do not move turtle. State and position of the turtle as well as drawings of other turtles are not affected.
        score_board.in_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        score_board.reset()
        snake.reset()


    if snake.head.ycor() > 280 or snake.head.ycor() < -295:
        score_board.reset()
        snake.reset()



    # Detect collision with tail
    """Method 1"""
    # for seg in range(1, len(snake.segments)):
    #     if snake.head.position() == snake.segments[seg].position():
    #         game_is_on = False
    #         score_board.gameover()

    """Method 2 using slicing"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


''' concept of using the update to refresh the screen,as well as using the timer
       to delay the refresh so that we can control how often it happens.'''
screen.exitonclick()
