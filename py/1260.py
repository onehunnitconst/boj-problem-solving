from sys import stdin

input = stdin.readline

graph = []

dfs_visited = []

bfs_visited = []

dfs_result = []

bfs_result = []

def dfs(graph, v, n):
  dfs_visited[v] = True
  dfs_result.append(v)
  for w in range(1, n+1):
    if graph[v][w] == 1 and graph[w][v] == 1 and not dfs_visited[w]:
      dfs(graph, w, n)


def bfs(graph, v, n):
  q = []
  bfs_visited[v] = True
  q.append(v)

  while len(q) > 0:
    v = q.pop(0)
    bfs_result.append(v)
    for w in range(1, n+1):
      if graph[v][w] == 1 and graph[w][v] == 1 and not bfs_visited[w]:
        q.append(w)
        bfs_visited[w] = True

n, m, v = list(map(int, input().rstrip().split()))

for _ in range(n+1):
  graph.append([0 for _ in range(n+1)])
  dfs_visited.append(False)
  bfs_visited.append(False)

for index in range(m):
  v1, v2 = list(map(int, input().rstrip().split()))
  graph[v1][v2] = 1
  graph[v2][v1] = 1

dfs(graph, v, n)
bfs(graph, v, n)

print(' '.join(list(map(str, dfs_result))))
print(' '.join(list(map(str, bfs_result))))