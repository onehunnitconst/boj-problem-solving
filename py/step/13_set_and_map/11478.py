# 11478: 서로 다른 부분 문자열의 개수

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + '\n')

def substring_count(s):
  substrs = set()

  for i in range(1, len(s)+1):
    for j in range(0, len(s)):
      substrs.add(s[j:j+i])
  
  return len(substrs)

print(substring_count(input()))