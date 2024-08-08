from turtle import Turtle, Screen
from Bullet import Bullet


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.penup()
        self.color('White')
        self.penup()
        self.speed(10)
        self.setposition(0, -250)
        self.screen = Screen()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)

    def move_left(self):
        self.backward(5)

    def move_right(self):
        self.forward(5)


