import turtle
import math

t = turtle.Turtle()
t.speed(50)
t.color("black")
turtle.bgcolor("pink")


def heart(n):
    x=15 * math.sin(n) ** 3
    y=13 * math.cos(n) - 5 * \
        math.cos(2*n) - 2*math.cos(3*n) - \
        math.cos(4*n)
    return x,y

t.penup()
for i in range(20):
    t.goto(0,0)
    t.pendown()
    for n in range (0, 100, 2):
        x,y = heart(n/15)
        t.goto(x*i, y*i)
    t.penup

t.hideturtle()
turtle.done
