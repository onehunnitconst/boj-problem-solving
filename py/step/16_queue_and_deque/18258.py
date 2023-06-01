# 18258: 큐 2
from sys import stdin, stdout
from collections import deque
input = lambda: stdin.readline().rstrip()
print = lambda s: stdout.write(str(s) + "\n")

n = int(input())
q = deque()

def push(element):
  q.append(element)
def pop():
  if empty():
    return -1
  return q.popleft()
def size():
  return len(q)
def empty():
  if (len(q) == 0):
    return 1
  return 0
def front():
  if empty():
    return -1
  return q[0]
def back():
  if empty():
    return -1
  return q[size() - 1]

for _ in range(n):
  command = input().split()
  if command[0] == "push":
    push(command[1])
  elif command[0] == "pop":
    print(pop())
  elif command[0] == "size":
    print(size())
  elif command[0] == "empty":
    print(empty())
  elif command[0] == "front":
    print(front())
  elif command[0] == "back":
    print(back())