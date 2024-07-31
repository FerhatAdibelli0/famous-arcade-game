from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
ball = Ball()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddy = Paddle((350, 0))
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


screen.exitonclick()
