# 1934: 최소공배수

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

# 최대공약수 (유클리드 호제법)
def gcd(a, b):
  if a < b:
    a, b = b, a
  while b > 0:
    tmp = a
    a = b
    b = tmp % b
  return a

# 최소공배수 (최대공약수를 활용하여 구하기)
def lcm(a, b):
  return a * b // gcd(a, b)

## 테스트 케이스 T
t = int(input())

## 테스트 케이스만큼 진행
for _ in range(t):
  a, b = map(int, input().split())
  print(lcm(a, b))