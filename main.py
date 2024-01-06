import time
from random import randint, choice
from turtle import Turtle, Screen

from car import Car
from race_turtle import Race_Turtle

is_moving = True
screen = Screen()
screen.setup(1200, 800)
screen.listen()
screen.colormode(255)
screen.tracer(0)

car_list = []
car_speed = 0.1


def move_up():
    race.green_turtle.forward(20)


race = Race_Turtle()
screen.onkeypress(fun=move_up, key="Up")


def gameover():
    game = Turtle()
    game.penup()
    game.hideturtle()
    game.goto(0, 0)
    game.color("Black")
    game.write(f"Game Over", move=False, align='center', font=('Arial', 28, 'normal'))


poss = ((640, -240), (640, -140), (640, 40), (640, 140), (640, 240),
        (900, -210), (860, -100), (800, 50),(900, 100),(940, 200),
        (1200, -190), (1100, -130), (1000, 80), (1150, 110), (1250, 250),
        (1500, -220),(1300, -180), (1400, 100), (1250, 40), (1300, 180),
        (1800, -250),(1600, -150), (1750, 110), (1550, 70), (1660, 220))


def create_many_car():
    for i in range(0,25):
        pos = ((640, -240), (640, -140), (640, 40), (640, 140), (640, 240),
                (900, -210), (860, -100), (800, 50), (900, 100), (940, 200),
                (1200, -190), (1100, -130), (1000, 80), (1150, 110), (1250, 250),
                (1500, -220), (1300, -180), (1400, 100), (1250, 40), (1300, 180),
               (1800, -250), (1600, -150), (1750, 110), (1550, 70), (1660, 220)
               )
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        colors = (r, g, b)
        a = Car()
        a.color(colors)
        car_list.append(a)
        car_list[i].goto(pos[i])


def collide():
    global is_moving
    for i in range(0, len(car_list)):
        if race.green_turtle.distance(car_list[i]) < 25:
            is_moving = False
            gameover()


create_many_car()

speed_move = 10
while is_moving:
    y = randint(-240, 240)
    x = randint(600, 620)
    speed = race.levelup()
    for i in range(0, len(car_list)):
        car_list[i].setheading(180)
        car_list[i].forward(speed_move)
        if car_list[i].xcor() < - 600:
            car_list[i].goto(poss[i])
        if speed is True:
            speed_move+=0.5
            car_list[i].forward(speed_move)
    collide()
    time.sleep(car_speed)
    screen.update()

screen.exitonclick()
