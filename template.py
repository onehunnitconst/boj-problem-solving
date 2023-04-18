from sys import stdin, stdout

# input, print 대신 표준 시스템 입출력 사용

def input_alt():
  return stdin.readline().rstrip()

def print_alt(s):
  return stdout.write(str(s) + "\n")

# 알고리즘 구현

# 메인 함수

n = int(input_alt())

# n, m = list(map(int, input_alt().split()))

print_alt(n)