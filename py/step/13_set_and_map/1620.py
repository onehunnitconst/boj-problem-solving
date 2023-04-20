# 1620: 나는야 포켓몬 마스터 이다솜

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

# 알고리즘 구현
def pokedex_queries(pokedex, queries):
  result = []
  for query in queries:
    result.append(pokedex[query])

  return map(str, result)

# 메인 함수
n, m = map(int, input().split())

pokedex = dict()

for key in range(1, n+1):
  pokemon = input()
  pokedex[str(key)] = pokemon
  pokedex[pokemon] = str(key)

queries = [input() for _ in range(m)]

print('\n'.join(pokedex_queries(pokedex, queries)))