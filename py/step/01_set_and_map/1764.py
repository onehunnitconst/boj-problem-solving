## 1764: 듣보잡

from sys import stdin, stdout
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + '\n')

n, m = map(int, input().split())

never_heard = set([input() for _ in range(n)])

never_seen = set([input() for _ in range(m)])

never_heard_seen = never_heard & never_seen

print(len(never_heard_seen))
print('\n'.join(sorted(never_heard_seen)))