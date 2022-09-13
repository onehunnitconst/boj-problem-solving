def isRight(compare: bool):
  return 'right' if compare else 'wrong'

while True:
  a, b, c = list(map(int, input().split()))
  if a == 0 and b == 0 and c == 0:
    break
  result = isRight((a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a))
  print(result)
