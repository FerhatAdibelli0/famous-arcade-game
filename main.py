from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
ball = Ball()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddy = Paddle((350, 0))
score_board = Score()
l_paddy = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddy.go_up, "Up")
screen.onkey(r_paddy.go_down, "Down")
screen.onkey(l_paddy.go_up, "w")
screen.onkey(l_paddy.go_down, "s")

is_going_on = True

while is_going_on:
    time.sleep(0.075)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with r_paddle
    if ball.distance(r_paddy) < 50 and ball.xcor() > 320 or ball.distance(l_paddy) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.start_ball()
        score_board.l_increase()
        score_board.update_scoreboard()

    if ball.xcor() < -380:
        ball.start_ball()
        score_board.r_increase()
        score_board.update_scoreboard()



screen.exitonclick()
