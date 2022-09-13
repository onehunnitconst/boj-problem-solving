t = int(input())

while t > 0:
  t = t - 1
  h, w, n = list(map(int, input().split()))
  floor = 1
  room = 1
  if h > 1 and w > 1:
    floor = (n-1) % h + 1
    room = (n-1) // h + 1
  elif h == 1:
    room = n
  elif w == 1:
    floor = n

  result = floor*100 + room
  print(result)