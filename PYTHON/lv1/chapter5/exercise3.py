number_1 = int(input('Enter number 1: '))
number_2 = int(input('Enter number 2: '))

for i in range(number_1, number_2 + 1):
  if(i % 3 == 0):
    print(i, end= ' ')

print()
print('result', number_1 * number_2)