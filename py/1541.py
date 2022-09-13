import sys
import re

input = sys.stdin.readline

expression = input().rstrip()

numbers = list(map(lambda x: x.lstrip('0'), re.split(r'[+-]', expression)))

operations = list(re.sub(r'[0-9]', '', expression))

if not expression[0].isdecimal():
  numbers.pop(0)
  numbers.insert(0, operations.pop(0))

for index in range(len(operations)):
  if not expression[0].isdecimal():
    numbers.insert(index*2+2, operations[index])
  else:
    numbers.insert(index*2+1, operations[index])

first = True
sub = 0

for index in range(len(numbers)):
  if numbers[index] == '-':
    if first:
      numbers[index] = '-('
      first = False
    else:
      numbers[index] = ')-('
    sub = sub + 1

if sub > 0:
  numbers.append(')')

print(eval(''.join(numbers)))