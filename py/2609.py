def euclidean(n, m):
  q = n
  r = m

  while r > 0:
    temp = q
    q = r
    r = temp % r
  
  return q

def gcd(n, m):
  return euclidean(m, n) if n < m else euclidean(n, m)

def lcm(n, m):
  return (int)(n * m / gcd(n, m))

n, m = list(map(int, input().split()))

print(gcd(n, m))
print(lcm(n, m))