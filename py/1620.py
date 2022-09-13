import sys

pokedex = {}
input = sys.stdin.readline

n, m = map(int, input().split())

for index in range(1, n+1):
  pokemon = input().rstrip()
  pokedex[str(index)] = pokemon
  pokedex[pokemon] = str(index)

for _ in range(m):
  query = input().rstrip()
  print(pokedex[query])