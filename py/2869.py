a, b, v = list(map(int, input().split()))

day = (v-b) // (a-b)
margin = (v-b) % (a-b)

if margin > 0:
  print(day+1)
else:
  print(day)
  
