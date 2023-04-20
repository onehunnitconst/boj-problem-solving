# 13241: 최소공배수

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

x1, y1 = map(int, input().split()) # x1 / y1
x2, y2 = map(int, input().split()) # x2 / y2

denominator = lcm(y1, y2)

numerator = (x1 * (denominator // y1)) + (x2 * (denominator // y2))

# 분자 분모를 둘의 최대공약수로 나눠주어야 함. 분수의 합이 기약분수가 아닐 수 있다
# 반례 2 3, 4 6
result_gcd = gcd(numerator, denominator)

print(str(numerator // result_gcd) + ' ' + str(denominator // result_gcd))