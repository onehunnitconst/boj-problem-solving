def isConstructor (n, m):
  sum = m
  m_str = str(m)
  for i in range(0, len(m_str)):
    sum = sum + int(m_str[i])
  return n == sum

n = int(input())
con = 0
ran = n-54 if n>54 else 0

for i in range (n>54, n):
  if isConstructor(n, i):
    con = i
    break

print(con)