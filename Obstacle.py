from turtle import Turtle


class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.x = -320
        self.y = -150

    def create_obstacle(self):
        for i in range(3):
            for j in range(15):
                new_aliens = Turtle("square")
                new_aliens.color("blue")
                new_aliens.penup()
                new_aliens.speed(5)
                new_aliens.goto(self.x, self.y)
                self.shearfactor(0.5)
                self.x += 50
                self.segments.append(new_aliens)

            self.x = -320
            self.y += 25