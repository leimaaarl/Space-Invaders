import time
from turtle import Screen
from Ship import Ship
from Alien import Aliens
from Bullet import Bullet
from Obstacle import Obstacle

screen = Screen()
screen.setup(height=600, width=680)
screen.bgcolor('Black')
screen.tracer(0)

ship = Ship()
alien = Aliens()
bullet = Bullet()
obstacle = Obstacle()

alien_bullet = Bullet()

alien.create_aliens()

obstacle.create_obstacle()

bullet_state = 'ready'

touched_right = False


def shoot():
    global bullet_state
    if bullet_state == 'ready':
        bullet_state = 'fired'
        bullet.goto(ship.xcor(), ship.ycor())


screen.listen()
screen.onkeypress(ship.move_left, 'Left')
screen.onkeypress(ship.move_right, 'Right')
screen.onkeypress(shoot, 'space')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if alien.segments[-1].xcor() <= 300 and not touched_right:
        alien.move_right()
    else:
        touched_right = True
        if alien.segments[0].xcor() >= -300 and touched_right:
            alien.move_left()
        else:
            if touched_right:
                alien.move_down()
                touched = 0

            touched_right = False

    if bullet_state == 'fired':
        bullet.showturtle()
        new_y = bullet.ycor()
        new_y += 20
        bullet.sety(new_y)

    if bullet.ycor() >= 320:
        bullet_state = 'ready'

    for i in range(len(alien.segments) - 1):
        if bullet.distance(alien.segments[i]) <= 15:
            alien.segments[i].hideturtle()
            bullet.goto(ship.xcor(), ship.ycor())
            bullet_state = 'ready'
            bullet.hideturtle()
            alien.segments.pop(i)

    for i in range(len(obstacle.segments) - 1):
        if bullet.distance(obstacle.segments[i]) <= 15:
            obstacle.segments[i].hideturtle()
            bullet.goto(ship.xcor(), ship.ycor())
            bullet_state = 'ready'
            bullet.hideturtle()
            obstacle.segments.pop(i)

    for i in range(len(alien.segments) - 1):
        if ship.distance(alien.segments[i]) <= 25:
            print("Game over")
            game_is_on = False


screen.exitonclick()
