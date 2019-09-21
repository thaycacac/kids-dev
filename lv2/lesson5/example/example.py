import turtle
import random
# thiết lập màn hình đồ họa
sc = turtle.Screen()
# thiết lập hình ảnh nền cho màn hình đồ họa 
sc.bgpic("bg1.gif")
# tạo nhân vật chim
play = 'bird0.gif'
turtle.register_shape(play)
turtle.shape(play)
# thiết lập chim rơi tự do
turtle.forward(100)
turtle.penup()

turtle.done()
