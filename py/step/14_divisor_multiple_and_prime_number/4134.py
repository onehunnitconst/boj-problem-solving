# 4134: 다음 소수
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


t = int(input())

for _ in range(t):
  n = int(input())
  while True:
    if is_prime_number(n) == True:
      print(n)
      break
    n = n + 1