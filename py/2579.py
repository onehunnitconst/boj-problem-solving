from sys import stdin
input = stdin.readline

stairs = []
max_scores = []

n = int(input().rstrip())

for index in range(n):
  stairs.append(int(input().rstrip()))

for index in range(n):
  if index == 0:
    max_scores.append(stairs[index])
  elif index == 1:
    max_scores.append(max(stairs[index-1], stairs[index-1] + stairs[index]))
  elif index == 2:
    max_scores.append(max(stairs[index-1] + stairs[index], stairs[index-2] + stairs[index]))
  elif index > 2:
    max_scores.append(max(max_scores[index-2]+ stairs[index], max_scores[index-3] + stairs[index-1] + stairs[index]))

print(max_scores.pop())