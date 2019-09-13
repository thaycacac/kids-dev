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
        
        self.forward(485)

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

turtle1 = Animal("yellow", 50)
turtle2 = Animal("green", 100)
turtle3 = Animal("blue", 0)
turtle4 = Animal("orange", -50)

turtle1.run()
    
