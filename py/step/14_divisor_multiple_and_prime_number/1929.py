# 1929: 소수 구하기
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

def is_prime_number(n):
  if n <= 1:
    return False
  index = 2
  while index ** 2 <= n:
    if n % index == 0:
      return False
    index = index + 1
  return True

m, n = map(int, input().split())

for num in range(m, n+1):
  if is_prime_number(num) == True:
    print(num)
  