import sys

input = sys.stdin.readline

exp = input().rstrip().split('-')

if len(exp[0]) == 0:
  exp[0] = '0'

res = 0

for index in range(len(exp)):
  temp_res = 0
  temp = list(map(lambda x: int(x.lstrip('0')), exp[index].split('+')))

  for el in temp:
    temp_res = temp_res + el

  if index == 0:
    res = res + temp_res
  else:
    res = res - temp_res

print(res)