n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))
blackjack = 0

for index1 in range (n-2):
  for index2 in range (index1 + 1, n-1):
    for index3 in range (index2 + 1, n):
      result = cards[index1] + cards[index2] + cards[index3];
      if result <= m:
        blackjack = max(
          blackjack,
          result
        )

print(blackjack)
