import turtle
import math
import random
import time
import game_easy

map_easy = [
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

map_medium = [
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

map_hard = [
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


def main():
    screen = turtle.Screen()
    screen.tracer(0)

    #register shape    
    easy = "easy.gif"
    medium = "medium.gif"
    hard = "hard.gif"
    screen.addshape(easy)
    screen.addshape(medium)
    screen.addshape(hard)

    #create level
    class Level(turtle.Turtle):

        level = ""

        def __init__(self, level, position_y):
            turtle.Turtle.__init__(self)
            self.shape(level)
            self.penup()
            self.goto(0, position_y)
            self.level = level
            self.onclick(self.play_game)

        def play_game(self, x, y):
            if self.level == "easy.gif":
                turtle.clearscreen()
                game_easy.init_game("easy", map_easy)
            elif self.level == "medium.gif":
                turtle.clearscreen()
                game_easy.init_game("medium", map_medium)
            else:
                turtle.clearscreen()
                game_easy.init_game("hard", map_hard)

    #add level
    level_easy = Level(easy, -120)
    level_medium = Level(medium, -170)
    level_hard = Level(hard, -220)

    screen.bgpic("introduction.png")
    screen.title("Maze Game")
    screen.setup(1000, 740)
    screen.tracer(0)

main()
