n = int(input())
rooms = 1

while n > 1:
  n -= rooms * 6
  rooms = rooms + 1

print(rooms)