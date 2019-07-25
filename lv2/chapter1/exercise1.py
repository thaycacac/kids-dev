import random

number_random = random.randrange(1, 100)
numer_guess = 0
print('Input you guess: ')
while number_random != numer_guess:
  numer_guess = (int)(input())
  if number_random > numer_guess:
    print('The number you guess is smaller')
  elif number_random < numer_guess:
    print('The number you guess is bigger')
  else:
    print('Congratulations you\'ve guessed correctly')

