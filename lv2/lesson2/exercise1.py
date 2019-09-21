def solve(a, b):
  return -int(b) / int(a)

print('input a: ')
a = input()
print('input b: ')
b = input()
if int(a) == 0 and int(b) != 0:
  print('no solution')
elif int(a) == 0 and  int(b) == 0:
  print('all numbers are solutions')
else:
  print('solution: ', solve(a,b))
