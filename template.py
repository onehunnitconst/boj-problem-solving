# input, print 대신 표준 시스템 입출력 사용

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

# 알고리즘 구현

# 메인 함수

n = int(input())

# n, m = list(map(int, input_alt().split()))

print(n)