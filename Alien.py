from turtle import Turtle


class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.x = -50
        self.y = 150

    def create_aliens(self):
        for i in range(3):
            for j in range(8):
                new_aliens = Turtle("circle")
                new_aliens.color("green")
                new_aliens.penup()
                new_aliens.speed(5)
                new_aliens.goto(self.x, self.y)
                self.shapesize(stretch_len=0.2, stretch_wid=0.2)
                self.x += 35
                self.segments.append(new_aliens)

            self.x = -50
            self.y += 25

    def move_right(self):
        for i in range(len(self.segments)):
            self.segments[i].fd(5)

    def move_left(self):
        for i in range(len(self.segments)):
            self.segments[i].back(5)

    def move_down(self):
        for i in range(len(self.segments)):
            self.segments[i].goto(self.segments[i].xcor(), self.segments[i].ycor() - 10)




