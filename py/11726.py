from sys import stdin

input = stdin.readline

tiling_method = []

n = int(input().rstrip())

for index in range(n+1):
  if index < 3:
    tiling_method.append(index)
  else:
    tiling_method.append(tiling_method[index-1] + tiling_method[index-2])

print(tiling_method[n] % 10007)