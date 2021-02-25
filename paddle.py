from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.resizemode('user')
        self.setpos(position)

    def go_up(self):
        self.sety(self.ycor() + 20)

    def go_down(self):
        self.sety(self.ycor() - 20)