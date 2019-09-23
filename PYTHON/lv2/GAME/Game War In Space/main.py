import turtle
import random
import math
import os

#set up screen
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Game 1")
#wn.bgpic("bg.png")
#wn.register_shape("heart.png")

class Game(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

    def play_sound(self, filename):
        os.system("afplay {}&".format(filename))

class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)

class Player(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("triangle")
        self.color("white")
        self.speed = 1

    def move(self):
        self.forward(self.speed)
        #check border
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1

    def decreasespeed(self):
        self.speed -= 1

class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        #self.shape("heart.png")
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)
        #check border
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

#check collision
def isCollision(t1, t2):
    a = t1.xcor() - t2.xcor()
    b = t2.ycor() - t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))
    if distance < 20:
        return True
    else:
        return False

#create instance
game = Game()
player = Player()
border = Border()

#draw border
border.draw_border()

#multiple goals
goals = []
for count in range(6):
    goals.append(Goal())

#set keyboard bindings
turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increasespeed, "Up")

#main
while True:
    wn.update()
    player.move()
    for goal in goals:
        goal.move()
        if isCollision(player, goal):
            goal.jump()
            game.change_score(10)
            #game.play_sound("collision")
    

