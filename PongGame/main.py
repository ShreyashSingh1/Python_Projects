"""
When problem is complex break it down into parts here we are dividing this game into 8 parts
1. Create the Screen
2. Create the paddle
3. Create another paddle
4. Create the ball and mave it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle is misses
8. Keep Score
My name is Shreyash
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
import linemaker

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)
line = linemaker.LineMaker()
ball = Ball()
score = ScoreBoard()

screen.onkeypress(paddle_r.paddle_up, "Up")
screen.onkeypress(paddle_r.paddle_down, "Down")
screen.onkeypress(paddle_l.paddle_up, "w")
screen.onkeypress(paddle_l.paddle_down, "s")

screen.tracer(0)
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()

    # Detect collision with upper wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_r) < 51 and ball.xcor() > 326 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_b()

    # Detect paddle_r misses
    if ball.xcor() > 380:
        ball.go_home()
        score.l_point()

    # Detect paddle_r misses
    if ball.xcor() < -380:
        ball.go_home()
        score.r_point()

screen.exitonclick()
