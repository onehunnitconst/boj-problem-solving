# 10815번: 숫자 카드

from sys import stdin, stdout

def input_alt():
  return stdin.readline().rstrip()

def print_alt(s):
  return stdout.write(str(s) + "\n")

# 알고리즘 구현
def cards_queries(cards, queries):
  results = []
  
  # ## 브루트 포스
  # for query in queries:
  #   result = 0
  #   for card in cards:
  #     if card == query:
  #       result = 1
  #       break
  #   results.append(result)
  
# 메인 함수
n = int(input_alt())

## list 대신 set?

cards = map(int, input_alt().split())

m = int(input_alt())

queries = map(int, input_alt().split())

results = cards_queries(set(sorted(cards)), queries)

print_alt(' '.join(list(map(str, results))))