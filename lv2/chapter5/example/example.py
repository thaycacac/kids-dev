import turtle
import random
# thiết lập màn hình đồ họa
sc = turtle.Screen()
#thiết lập hình ảnh nền cho màn hình đồ họa 
sc.bgpic("background.png")
# Vẽ vùng giới hạn di chuyển: 
mypen = turtle.Turtle() 
mypen.penup() 
mypen.setposition(-300, -300) 
mypen.pendown() 
mypen.pensize(3) 
mypen.speed(0)
for i in range(4): 
    mypen.forward(600) 
    mypen.left(90)
# vẽ xong, ẩn đối tượng vẽ
mypen.hideturtle()
# Tạo ra nhân vật siêu anh hùng
player = turtle.Turtle() 
player.color("yellow") 
player.shape("turtle") 
player.penup()
# thiết lập tốc độ siêu anh hùng
speed = 1
# định nghĩa các phím ra chuyển
def turnleft(): player.left(30)
def turnright(): player.right(30)
def increaseSpeed(): 
    global speed 
    speed += 1
    if speed >= 5:
        speed = 5
def decreaseSpeed(): 
    global speed 
    speed -= 1
    if speed <= -5:
        speed = -5
# khi nhấn phím
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increaseSpeed, "Up") 
turtle.onkey(decreaseSpeed, "Down")
# Xử lý khi siêu anh hùng di chuyển va chạm vào biên 
while True:
# thiết lập siêu anh hùng tiến về phía trước
    player.forward(speed)
#kiểm tra xem khi di chuyển có chạm biên không 
    if player.xcor() < -290 or player.xcor() > 290:
        player.right(180)
    if player.ycor() < -290 or player.ycor() > 290:
        player.right(180)

turtle.done()