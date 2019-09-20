import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("A Maze Game")
screen.setup(700, 700)
screen.tracer(0)

#register shape
#turtle.shape("wizard_right.gif")
#turtle.shape("wizard_left.gif")
#turtle.shape("treasure.gif")
#turtle.shape("wall.gif")

# create list
levels = []
walls = []
treasures = []
enemies = []

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#create player
class Player(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
        
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

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 5:
            return True
        else:
            return False

#create treasure
class Treasure(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#class enemy
class Enemy(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = -25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            x = 0
            y = 24
        elif self.direction == "down":
            x = 0
            y = -24
        elif self.direction == "left":
            x = -24
            y = 0
        elif self.direction == "right":
            x = 24
            y = 0
        move_to_x = self.xcor() + x
        move_to_y = self.ycor() + y

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])
        turtle.ontimer(self.move, t = random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#lv1
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXXE         XXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X      XX  XXX        XXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"XE               XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX        TXXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXXE             X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX     E   XXXX        XX",
"XXXX               T    X",
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
            elif character == "T":
                treasures.append(Treasure(position_x, position_y))
            elif character == "E":
                enemies.append(Enemy(position_x, position_y))

#create instance
pen = Pen()
player = Player()

print(len(enemies))

#keyboard bindding
turtle.listen()
turtle.onkey(player.up, "Up")
turtle.onkey(player.down, "Down")
turtle.onkey(player.right, "Right")
turtle.onkey(player.left, "Left")

#set up level
setup_maze(levels[0])

#run enemy
for enemy in enemies:
    turtle.ontimer(enemy.move, 250)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print('Play gold: {}'.format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    for enemy in enemies:
        if player.is_collision(enemy):
            print('Player dead!!!')
            break
    screen.update()


