# 1269: 대칭 차집합

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + '\n')

n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

num_of_symmetric_difference = lambda a, b: len((a - b) | (b - a))

print(num_of_symmetric_difference(a, b))