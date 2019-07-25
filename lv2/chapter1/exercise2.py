import random

number_random = random.randrange(1, 100)
numer_guess = 0
count = 0
print('Input you guess: ')
while number_random != numer_guess:
  numer_guess = (int)(input())
  if number_random > numer_guess:
    print('The number you guess is smaller')
    count += 1
  elif number_random < numer_guess:
    print('The number you guess is bigger')
    count += 1
  else:
    print('Congratulations you\'ve guessed correctly')
print('You guessed wrong:', count)
