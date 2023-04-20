from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle()
r_paddle.pad_side(350)
l_paddle = Paddle()
l_paddle.pad_side(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # hit the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # hit a pad
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.hit_pad()

    # misses a pad and get a score
    if ball.xcor() > 400:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_pos()
        scoreboard.r_point()

    # check if either player has reached 5 points
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False

# display the winner
if scoreboard.l_score == 5:
    print("Left player wins!")
else:
    print("Right player wins!")

screen.exitonclick()
