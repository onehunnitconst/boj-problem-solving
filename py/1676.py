from sys import stdin
input = stdin.readline

n = int(input().rstrip())

fives = 0

for index in range(1, n+1):
  el = index
  while el % 5 == 0:
    el = el // 5
    fives = fives + 1

print(fives)