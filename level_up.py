from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super(Level, self).__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.pendown()
        self.write("FINISHING POINT", align="center", font=("Arial", 18, "normal"))
        self.penup()
        self.goto(0, -295)
        self.pendown()
        self.write("STARTING POSITION", align="center", font=("Arial", 18, "normal"))
        self.penup()
        self.score = 0
        self.set = 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER \n YOUR SCORE : {self.score}", align="center", font=("Arial", 28, "normal"))
        self.penup()

    def next_level(self):
        self.set += 1
        self.goto(0, 0)
        self.pendown()
        self.color("red")
        self.write(f"LEVEL {self.set}",align="center", font=("Arial", 30, "normal"))
        self.color("white")
        self.penup()
        self.clear()

    def show_score(self):
        self.penup()
        self.goto(-300, 280)
        self.pendown()
        self.write(f"LEVE : {self.set}", font=("Arial", 20, "normal"))
        self.penup()
