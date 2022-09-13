from sys import stdin
input = stdin.readline

def heapify(arr, count):
  for index in range(count, -1, -1):
    siftDown(arr, index, count - 1)

def siftDown(arr, start, end):
  root = start
  while True:
    child = (root * 2) + 1
    if child > end:
      break
    if child + 1 <= end and arr[child] < arr[child + 1]:
      child += 1
    if arr[root][0] < arr[child][0] or (arr[root][0] == arr[child][0] and arr[root][1] < arr[child][1]):
      arr[root], arr[child] = arr[child], arr[root]
      root = child
    else:
      break

def heapsort(arr, count):
  heapify(arr, count)
  for index in range(count-1, -1, -1):
    arr[0], arr[index] = arr[index], arr[0]
    siftDown(arr, 0, index - 1)
    

n = int(input().rstrip())
v = []

for index in range(n):
  x, y = map(int, input().rstrip().split())
  v.append((x, y))

heapsort(v, len(v))

for index in range(n):
  print(v[index][0], v[index][1])