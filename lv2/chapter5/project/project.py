import turtle

screen = turtle.Screen()
screen.setup(350, 500)
screen.bgpic("background.png")
bird =  turtle.Turtle()
bird.shape("triangle")

move_speed = 10
turn_speed = 10

def forward(): bird.forward(move_speed)
def backward(): bird.backward(move_speed)
def left(): bird.left(turn_speed)
def right(): bird.right(turn_speed)

screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

turtle.done()

