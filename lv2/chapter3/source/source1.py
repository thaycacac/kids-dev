def add(a, b):
    print('a + b = ', a + b)
    return a + b
def subtract(a, b):
    print('a - b = ', a - b)
    return a - b
def multiply(a, b):
    print('a * b = ', a * b)
    return a * b
def divide(a, b):
    print('a / b = ', a / b)
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print('Age: %d, Height: %d, Weight: %d, IQ: %d', age, height, weight, iq)
