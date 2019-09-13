import turtle
import random

screen = turtle.Screen()
screen.bgcolor("red")
screen.title("Game Turtle")

class Animal(turtle.Turtle):
    
    def __init__(self, color, pos):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color(color)
        self.shape("turtle")
        self.goto(-300, pos)

    def run(self):
        self.speed(1)
        self.pendown()
        self.forward(10)

class Flag(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw(self):
        self.penup()
        self.goto(200, 200)
        self.pendown()
        self.sety(-200)

#draw flag
flag = Flag()
flag.draw()

turtles = []
turtles.append(Animal("yellow", 50))
turtles.append(Animal("green", 100))
turtles.append(Animal("blue", 0))
turtles.append(Animal("orange", -50))

while True:
    number = random.randint(0, 4)
    turtles[number - 1].run()
    if turtles[number-1].xcor() >= 185:
        break
    
