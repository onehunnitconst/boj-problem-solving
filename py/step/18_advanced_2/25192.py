# 25192: 인사성 밝은 곰곰이
from functools import reduce
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

n = int(input())

gomgom = []
new_member = 0

for _ in range(n):
  user = input()
  if user == 'ENTER':
    new_member = new_member + 1
    gomgom.append(set())
  else:
    gomgom[new_member - 1].add(user)

result = reduce(lambda a, b: a+b, map(lambda s: len(s), gomgom), 0)

print(result)