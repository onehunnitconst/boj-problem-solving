def case():
  memo = []
  k = int(input())
  n = int(input())

  for i in range(1, n+1):
    memo.append(i)

  for i in range(1, k+1):
    for j in range (1, n):
      memo[j] = memo[j-1] + memo[j]
  
  print(memo[n-1])


t = int(input())

for tc in range(t):
  case()
