import turtle
import random

screen = turtle.Screen()
screen.bgcolor("red")

t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.color("green")
t.speed(0)
t.goto(-200, 50)

t1 = turtle.Turtle()
t1.penup()
t1.shape("turtle")
t1.color("blue")
t1.speed(0)
t1.goto(-200, 0)

t2 = turtle.Turtle()
t2.penup()
t2.shape("turtle")
t2.color("orange")
t2.speed(0)
t2.goto(-200, -50)


t3 = turtle.Turtle()
t3.penup()
t3.shape("turtle")
t3.color("yellow")
t3.speed(0)
t3.goto(-200, -100)

t4 = turtle.Turtle()
t4.hideturtle()
t4.penup()
t4.shape("circle")
t4.color("white")
t4.speed(0)
t4.goto(200, 150)
t4.pendown()
t4.pensize(5)
t4.right(90)
t4.forward(350)

while True:
    a = random.randint(1, 4)
    if a == 1:
        t.forward(3)
        if t.xcor() >= 187:
            break
    elif a == 2:
        t1.forward(3)
        if t1.xcor() >= 187:
            break
    elif a == 3:
        t2.forward(3)
        if t2.xcor() >= 187:
            break
    else:
        t3.forward(3)
        if t3.xcor() >= 187:
            break
