# 4948: 베르트랑 공준
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

max = 123456 * 2
prime_numbers = [True for _ in range(max + 1)]

prime_numbers[0] = False
prime_numbers[1] = False
index = 2

while index ** 2 <= max:
  if prime_numbers[index] == True:
    for sub in range(index+1, max+1):
      if sub % index == 0:
        prime_numbers[sub] = False
  index = index + 1

while True:
  n = int(input())
  result = 0
  if n == 0:
    break
  filtered = list(filter(lambda x: x == True, prime_numbers[n+1:2*n+1]))
  print(len(filtered))
  