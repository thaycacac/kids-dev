number = int(input('Enter number: '))
sum = 0
for i in range(number + 1):
  sum += i
print('sum: ', sum)

for i in range(1, number + 1, 2):
  print(i, end=" ")

print()
sum = 0
for i in range(1, number + 1, 2):
  sum += i
print('sum: ', sum)
