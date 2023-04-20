# 2485: 가로수

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

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

# 첫 번째 가로수의 위치를 0으로 둔다면 마지막 가로수의 조정 위치는 첫 번째 가로수의 위치만큼 빼야 함.
# 마지막 가로수의 조정 위치를 가로수 사이의 거리로 나누고, 1을 더하면 나무가 몇 그루 필요한 지 나온다.
# 여기서 기존 가로수의 개수를 빼면 결과가 나옴
def get_result(n, first_tree, last_tree, gap):
  return ((last_tree - first_tree) // gap) + 1 - n

n = int(input())

roadside_trees = [int(input()) for _ in range(n)]

roadside_trees.sort()

print(get_result(n, roadside_trees[0], roadside_trees[n-1], gap(roadside_trees)))