from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Build the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Build our game objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Draw the center-line
center_line = Turtle(shape='square')
center_line.penup()
center_line.goto(0, 410)
center_line.color('white')
center_line.setheading(270)
center_line.forward(25)
while center_line.ycor() > -410:
    center_line.pendown()
    center_line.forward(50)
    center_line.penup()
    center_line.forward(50)

# Set-up our key bindings
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Start the main loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball bounces
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right side miss
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()
        ball.bounce_x()

    # Detect left sided miss
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()
        ball.bounce_x()
