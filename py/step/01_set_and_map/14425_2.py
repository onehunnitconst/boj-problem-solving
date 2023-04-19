# 14425번: 문자열 집합

from sys import stdin, stdout

def input_alt():
  return stdin.readline().rstrip()

def print_alt(s):
  return stdout.write(str(s) + "\n")

# 알고리즘 구현
def strings_queries(strings, queries):
  result = 0

  for query in queries:
    if query in strings:
      result += 1

  return result

# 메인 함수
n, m = list(map(int, input_alt().split()))

strings = [str(input_alt()) for _ in range(n)]

queries = [str(input_alt()) for _ in range(m)]

result = strings_queries(set(strings), queries)

print_alt(result)