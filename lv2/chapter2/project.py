question = 'This is question'
answers = ['a', 'b', 'c', 'd', 'e']
answer_correct = 'd'

def test(anwer_user):
  if answer_user == answer_correct:
    print('correct')
  else:
    print('incorrect')

print(question)
for answer in answers:
  print(answer)

print('Enter your answer: ')
answer_user = input()
test(answer_user)