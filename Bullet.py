from turtle import Turtle, Screen

screen = Screen()


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.2, stretch_wid=0.2)
        self.shape('square')
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed(5)
        self.setheading(90)



