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

#walls
walls = []

#create player
class Player(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        
    def up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

#create levels list
levels = []

#lv1
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXX          XXXX",
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
                #add coordinates to wall list
                walls.append((position_x, position_y))
            elif character == "P":
                player.goto(position_x, position_y)

#create instance
pen = Pen()
player = Player()

#keyboard bindding
turtle.listen()
turtle.onkey(player.up, "Up")
turtle.onkey(player.down, "Down")
turtle.onkey(player.right, "Right")
turtle.onkey(player.left, "Left")

#set up level
setup_maze(levels[0])


