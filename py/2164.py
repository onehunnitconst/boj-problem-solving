from collections import deque

cards = deque()

n = int(input())

for i in range(0, int(n/2)): 
  cards.append((i+1)*2)

if n == 1:
  print(1)
else:
  if n % 2 != 0:
    cards.append(cards.popleft())
  while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
  print(cards.pop())
