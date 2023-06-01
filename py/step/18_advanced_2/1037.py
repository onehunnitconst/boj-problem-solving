# 1037: 약수
from functools import reduce
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

n = int(input())

divisors = list(map(int, input().split()))

divisors.sort()

first = divisors[0]
last = divisors[len(divisors) - 1]

print(first * last)