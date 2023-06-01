# 20920: 영단어 암기는 괴로워
from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

n, m = map(int, input().split())

words = dict()

for _ in range(n):
  word = input()
  if len(word) >= m:
    if words.get(word) is None:
      words[word] = 1
    else:
      words[word] = words[word] + 1

def sorted_key(item):
  frequency_desc = -item[1]
  length_desc = -len(item[0])
  lexicographical_asc = item[0]
  return (frequency_desc, length_desc, lexicographical_asc)

sorted_words = sorted(
  words.items(),
  key=sorted_key
)

for item in sorted_words:
  print(item[0])