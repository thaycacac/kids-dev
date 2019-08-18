# BÀI 1
# --------------------------------------------

# Khai báo hàm
def hello():
    print('xin chao moi nguoi')

# Sử dụng hàm
hello()

# Hàm có tham số
def sum(a, b):
    print('tong hai so là: ', a + b)
sum(10, 20)

# BÀI 2
# --------------------------------------------

# Hàm trả về
def multiply(a, b):
    return a * b
print('tich hai so là: ', multiply(2, 3))

# Phạm vi biến của hàm

# Thay đổi giá trị biến ngoài hàm

a = 'tôi là biến ngoài hàm'
def say_():
    global a
    a = 'tôi là biến trong hàm'

# Tham số mặc định
def tinh_tong(a=2, b=3):
  return a + b
print(‘tham số mặc định: ’, tinh_tong())
print(‘có mặc định: ’, tinh_tong(10, 20))


# Truyền vô tham số
def get_sum(*number):
	sum = 0
	for i in number:
		sum += i
return sum
result = get_sum(1, 2, 3, 4)
print(‘Tổng là: ’result)

# BÀI 3
# --------------------------------------------

# Tạo module
"""
Bước 1: Tạo một thư mục bất kỳ lưu lại ổ đĩa
Bước 2: Lưu tên file trong thư mục ở bước 1 (ví dụ: my_math.py ) , viết hàm trong file này và lưu file
Bước 3: import my_math và sử dụng các hàm trong my_math'''
"""

# Sử dụng một số hàm cụ thể trong module
from module import function1, function2,…

# Định danh cho module
import module as name 
from module import function as name 

# Module random trong python
import random

random.randrange(100)
random.randrange(0, 100)
random.randrange(0, 100, 3)


# BÀI 4
# --------------------------------------------

# Import module turtle
import turtle

# Khai báo màn hình đồ họa của turtle
screen = turtle.Screen()

# Thiết lập màu nền
screen.bgcolor(“blue”)

# Khởi tạo đối tượng đồ họa
t = turtle.Turtle()

# Khởi tạo đối tượng với các hình dạng
t.shape(“circle”)

# Tiến về phía trước tọa độ 100
t.forward(100)

# Di chuyển tới vị trí tọa độ (100, 0)
t.goto(100,0)

# Quay phải 90 độ
t.right(90): 

# Quay trái 90 độ
t.left(90)

# Muốn đối tượng đồ họa di chuyển không vẽ thì ta chỉ cần sử dụng hàm
t.penup()

# Muốn đối tượng đồ họa di chuyển và vẽ thì ta sử dụng hàm
t.pendown()






