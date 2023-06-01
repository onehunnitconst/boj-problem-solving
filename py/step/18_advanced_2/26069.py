# 25192: 붙임성 좋은 총총이
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

n = int(input())
rainbow_dance = dict()
rainbow_dance['ChongChong'] = True

for _ in range(n):
  a, b = input().split()

  if rainbow_dance.get(a) is True:
    rainbow_dance[b] = True
  elif rainbow_dance.get(b) is True:
    rainbow_dance[a] = True
  else:
    rainbow_dance[a] = False
    rainbow_dance[b] = False

result = len(list(filter(lambda x: x is True, rainbow_dance.values())))

print(result)