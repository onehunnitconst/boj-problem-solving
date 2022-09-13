n = int(input())
people = []
pairs = 0

for _ in range(0, n):
  people.append(int(input()))

for front in range(0, n-1):
  for rear in range(front+1, n):
    pairs = pairs + 1
    if people[front] < people[rear]:
      break

print(pairs)