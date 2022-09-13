n, k = map(int, input().split())
circle = []
josephus = []

for index in range(n):
  circle.append(index + 1)

for _ in range(n):
  for index in range(k):
    first = circle.pop(0)
    if index < k - 1:
      circle.append(first)
    else:
       josephus.append(first)


print(repr(josephus).replace('[', '<').replace(']', '>'))