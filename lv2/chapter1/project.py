print('input income:')
income = (int)(input())

print('input outcome:')
print('study: ')
study = (int)(input())
print('entertaiment: ')
entertaiment = (int)(input())
print('eating: ')
eating = (int)(input())

# Displays the total amount spent, the remaining amount
total = study + entertaiment + eating
print('total', total)

# Show chart with expenditure
print('study', study)
print('entertaiment', entertaiment)
print('eating', eating)

if entertaiment > study:
  print ('You need focus study')
if entertaiment > eating:
  print('You need to pay attention to health')
# you need add more