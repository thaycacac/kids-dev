income = float(input('Enter the amount you want to send: '))
years = int(input('Enter the number of years you want to send: '))

outcome = income
for year in range(years):
  outcome += outcome * 0.12

print('Outcome: ', outcome)

for year in range(years):
  outcome += outcome * 0.12
  outcome -= outcome * 9 / 10

print('Outcome: ', outcome)