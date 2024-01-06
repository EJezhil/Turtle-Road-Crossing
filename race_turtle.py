from turtle import Turtle

from car import Car


class Race_Turtle():
    x = -580
    y = 300
    LEVEL = 1
    def __init__(self):
        self.create_turtle()
        self.show_line()
        self.show_level()
    def create_turtle(self):
        self.green_turtle = Turtle()
        self.green_turtle.penup()
        self.green_turtle.shapesize(2,2)
        self.green_turtle.shape("turtle")
        self.green_turtle.color("green")
        self.green_turtle.goto(0, -300)
        self.green_turtle.setheading(90)
        self.green_turtle.shape("turtle")

    def show_line(self):
        for i in range (0,30):
            self.line = Turtle()
            self.line.penup()
            self.line.shape("square")
            self.line.shapesize(stretch_wid=0.2, stretch_len=0.8)
            self.line.color("green")
            self.line.goto(self.x,self.y)
            self.x += 40

    def show_level(self):
        self.level = Turtle()
        self.level.hideturtle()
        self.level.penup()
        self.level.goto(-580, 340)
        self.level.write(f"Level: {self.LEVEL}", font=("Arial",20,"normal"))

    def levelup(self):
        if self.green_turtle.ycor() >= 300:
            self.LEVEL += 1
            self.level.clear()
            self.show_level()
            print(self.LEVEL)
            self.green_turtle.goto(0, -300)
            return True

