text = input('Enter paragraph: ')
length = len(text) - 1
for i in range(0, length + 1):
  text = text + text[length - i]
text = text[length + 1:]
print('Result: ', text)