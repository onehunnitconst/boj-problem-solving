from sys import stdin
input = stdin.readline

class Stack:
  def __init__(self):
    self.stack = []
  def push(self, num):
    self.stack.append(num)
  def pop(self):
    if len(self.stack) > 0:
      print(self.stack.pop())
    else:
      print(-1)
  def top(self):
    if len(self.stack) > 0:
      print(self.stack[-1])
    else:
      print(-1)
  def size(self):
    print(len(self.stack))
  def empty(self):
    print(1 if len(self.stack) == 0 else 0)


n = int(input().rstrip())
stack = Stack()

for index in range(n):
  command = input().rstrip().split()
  if command[0] == 'push':
    stack.push(int(command[1]))
  elif command[0] == 'pop':
    stack.pop()
  elif command[0] == 'top':
    stack.top()
  elif command[0] == 'size':
    stack.size()
  elif command[0] == 'empty':
    stack.empty()


