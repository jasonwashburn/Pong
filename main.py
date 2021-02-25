from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

right_paddle = Paddle()

screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

screen.exitonclick()