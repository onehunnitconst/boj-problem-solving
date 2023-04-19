# 10815번: 숫자 카드

from sys import stdin, stdout

def input_alt():
  return stdin.readline().rstrip()

def print_alt(s):
  return stdout.write(str(s) + "\n")

# 알고리즘 구현
def cards_queries(cards, queries):
  results = []
  
  for query in queries:
    result = 0
    first, last = 0, len(cards) - 1
    while first <= last:
      mid = (first + last) // 2
      if cards[mid] > query:
        last = mid-1
      elif cards[mid] < query:
        first = mid+1
      else:
        result = 1
        break
    results.append(result)

  return results

# 메인 함수
n = int(input_alt())

cards = set(map(int, input_alt().split()))

m = int(input_alt())

queries = map(int, input_alt().split())

results = cards_queries(sorted(cards), queries)

print_alt(' '.join(list(map(str, results))))