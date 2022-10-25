from turtle import Turtle
import random


color = ["red", "green", "blue", "lime", "yellow"]


class UserPen(Turtle):
    def __init__(self):
        super(UserPen, self).__init__()
        self.color(random.choice(color))
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_len=0.7, stretch_wid=1)
        self.left(90)
        self.initial_location()

    def initial_location(self):
        self.goto(0, -280)

    def move_up(self):
        if self.ycor() < 281:
            self.forward(10)
        else:
            self.goto(0, 280)

    def move_down(self):
        if self.ycor() > -281:
            self.backward(10)
        else:
            self.goto(0, -280)
