from turtle import Turtle
import random


class Car:
    def __init__(self):
        self.cars = []
        self.color = ["red", "blue", "green", "white", "lime"]
        self.pos = []
        for p in range (-240, 260, 20):
            self.pos.append(p)

    def creat_car(self):
            pen = Turtle()
            pen.penup()
            pen.shape("square")
            pen.color(random.choice(self.color))
            pen.shapesize(stretch_len=2, stretch_wid=1)
            pen.goto(300, random.choice(self.pos))
            pen.setheading(180)
            self.cars.append(pen)

    def move(self, y):
        for i in self.cars:
            if i.xcor() > -300:
                i.forward(20 + y)
            else:
                i.color("black")
                self.cars.remove(i)
                del i
