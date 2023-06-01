# 2108: 통계학
from functools import reduce
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

def get_mean(numbers):
  return round(reduce(lambda a, b: a+b, numbers) / len(numbers))

def get_median(numbers):
  return numbers[len(numbers) // 2]

def get_mode(numbers):
  counts = dict()

  for number in numbers:
    if counts.get(number) is None:
      counts[number] = 1
    else:
      counts[number] = counts[number] + 1

  sorted_map = sorted(
    counts.items(),
    key=lambda item: (-item[1], item[0])
  )

  max_count = sorted_map[0][1]
  
  modes = list(filter(lambda x: x[1] is max_count, sorted_map))

  if len(modes) == 1:
    return modes[0][0]
  else:
    return modes[1][0]

def get_range(numbers):
  first = numbers[0]
  last = numbers[len(numbers) - 1]
  return last - first

n = int(input())

numbers = sorted([int(input()) for _ in range(n)])

print(get_mean(numbers))
print(get_median(numbers))
print(get_mode(numbers))
print(get_range(numbers))