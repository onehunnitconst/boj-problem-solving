def gcd(a, b):
  if a < b:
    a, b = b, a
  while b > 0:
    tmp = a
    a = b
    b = tmp % b
  return a

def gap(roadside_trees):
  gap = roadside_trees[1] - roadside_trees[0]
  for index in range(2, len(roadside_trees)):
    gap = gcd(roadside_trees[index] - roadside_trees[0], gap)
  return gap


n = int(input())

roadside_trees = []

for _ in range(n):
  roadside_trees.append(int(input()))

roadside_trees.sort()

pivot = roadside_trees[0]
trees_gap = gap(roadside_trees)
result = 0

roadside_trees_set = set(roadside_trees)

while pivot <= roadside_trees[len(roadside_trees) - 1]:
  if pivot not in roadside_trees_set:
    result = result + 1
  pivot = pivot + trees_gap

print(result)