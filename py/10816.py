import sys

input = sys.stdin.readline

n = int(input().rstrip())

cards = list(map(str, input().split()))

cards_dict = {}

for index in range(n):
  if cards[index] in cards_dict:
    cards_dict[cards[index]] = cards_dict[cards[index]] + 1
  else:
    cards_dict[cards[index]] = 1

m = int(input().rstrip())

query_cards = list(map(str, input().split()))

output = []

for index in range(m):
  if query_cards[index] in cards_dict:
    output.append(str(cards_dict[query_cards[index]]))
  else:
    output.append(str(0))

print(' '.join(output))