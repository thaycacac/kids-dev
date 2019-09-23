number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))
number3 = int(input('Enter number 3: '))
number4 = int(input('Enter number 4: '))
number5 = int(input('Enter number 5: '))

if (number1 > number2 and number1 > number3 and number1 > number4 and number1 > number5):
  print('max: ', number1)
elif (number2 > number1 and number2 > number3 and number2 > number4 and number2 > number5):
  print('max: ', number2)
elif (number3 > number1 and number3 > number2 and number3 > number4 and number3 > number5):
  print('max: ', number3)
elif (number4 > number1 and number4 > number2 and number4 > number3 and number4 > number5):
  print('max: ', number4)
else:
  print('max: ', number5)

if (number1 < number2 and number1 < number3 and number1 < number4 and number1 < number5):
  print('min: ', number1)
elif (number2 < number1 and number2 < number3 and number2 < number4 and number2 < number5):
  print('min: ', number2)
elif (number3 < number1 and number3 < number2 and number3 < number4 and number3 < number5):
  print('min: ', number3)
elif (number4 < number1 and number4 < number2 and number4 < number3 and number4 < number5):
  print('min: ', number4)
else:
  print('min: ', number5)