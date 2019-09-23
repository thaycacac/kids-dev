from random import *

number_random = 0
count_wrong = 0

while True:
  for i in range(5):
    if(count_wrong == 0): 
      number_random = randint(1, 300)
    guess = int(input('Enter number: '))
    if(number_random == guess):
      print('You have correctly predicted the number ', number_random)
    elif(number_random - 10 < guess and guess < number_random + 10):
      print('You guessed it right!')
    else:
      count_wrong += 1
      print('You answered incorrectly ' + str(count_wrong) + ' times')
    if(count_wrong == 5):
      count_wrong = 0
      print('You guessed wrong all five times, the results changed. Please guess again')
