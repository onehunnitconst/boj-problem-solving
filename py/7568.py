n = int(input())
people = []
rank = []

for index in range(0, n):
  x, y = list(map(int, input().split()))
  people.append([x, y])
  rank.append(1)

for index in range(0, n):
  for subIndex in range(0, n):
    if index == subIndex:
      continue
    if people[index][0] < people[subIndex][0] and people[index][1] < people[subIndex][1]:
      rank[index] = rank[index] + 1

print(' '.join(str(element) for element in rank))