print('* **********************************')
print('* VER POINT MANAGEMENT SOFTWARE 1.0 *')
print('* Creat by: Pham Ngoc Hoa           *')
print('* ********************************* *')

while True:
  math = float(input('Enter math grade: '))
  literature = float(input('Enter the score of literature: '))
  english = float(input('Enter the English language score: '))
  avg = (math + literature + english) / 3
  print('Avg: ', avg)
  if(avg >= 8.0): print('You study very well. Gaining Good Students')
  elif(avg >= 9.0): print('You are excellent')
  elif(avg>=7 and avg <8): print('You study well')
  elif(avg>=5 and avg<7): print('You study average')
  elif(avg<5): print('You are poor')
  check = int(input('Press 1 to continue, 0 to exit: '))
  if(check == 0): break

