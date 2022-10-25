from turtle import Screen, Turtle
from time import sleep
from user_pen import UserPen
from  cars import Car
from level_up import Level


screen = Screen()
screen.setup(width=600, height=620)
screen.bgcolor("black")
screen.tracer(0)
screen.title("ROAD CROSSING GAME")
line = Turtle()
user_pen = UserPen()
car = Car()
level = Level()


def draw_line():
    line.color("white")
    line.penup()
    line.hideturtle()
    line.goto(-300, -260)
    line.pensize(20)
    line.pendown()
    line.fd(600)
    line.penup()
    line.goto(-300, 260)
    line.pendown()
    line.forward(600)


draw_line()
screen.onkeypress(fun=user_pen.move_up, key="w")
screen.onkeypress(fun=user_pen.move_down, key="s")
x = 0
y = 1
while True:
    screen.update()
    car.creat_car()
    level.show_score()
    car.move(y)

    x += 1
    if x >= 20:
        sleep(0.1)
        screen.listen()
    else:
        sleep(0.01)

    for pen in car.cars:
        if pen.distance(user_pen) < 17:
            level.game_over()
            screen.exitonclick()

    if user_pen.ycor() >= 280:
        level.next_level()
        sleep(2)
        user_pen.initial_location()
        y += 5
