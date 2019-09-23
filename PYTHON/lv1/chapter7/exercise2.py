paragraph = input('Enter paragraph: ')
print('Not formatted: ', paragraph)
while(paragraph[len(paragraph) - 1] == ' '):
  paragraph = paragraph[: len(paragraph) - 1]
while(paragraph[0] == ' '):
  paragraph = paragraph[1:]
while(paragraph.find('  ') != -1):
  paragraph = paragraph.replace('  ', ' ')
print('Formatted: ', paragraph)