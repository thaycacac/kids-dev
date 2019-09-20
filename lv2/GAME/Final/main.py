import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("A Maze Game")
screen.setup(700, 700)

#register shape
#turtle.shape("wizard_right.gif")
#turtle.shape("wizard_left.gif")
#turtle.shape("treasure.gif")
#turtle.shape("wall.gif")

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#create levels list
levels = []

#lv1
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#add level
levels.append(level_1)

#setup level
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            position_x = -288 + (x * 24)
            position_y = 288 - (y * 24)
            if character == "X":
                pen.goto(position_x, position_y)
                pen.stamp()

#create instance
pen = Pen()

#set up level
setup_maze(levels[0])


