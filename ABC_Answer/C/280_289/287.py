import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
if N == 1 and M == 0:
  print('Yes')
  exit()

G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * (N+1)
visited[0] = True
def dfs(node):
    visited[node] = True

    for to in G[node]:
        if visited[to] == False:
            dfs(to)


sg = []
for i, g in enumerate(G):
  if len(g) == 1:
    sg.append(i)
  elif len(g) > 2:
    print('No')
    exit()

if len(sg) != 2:
  print('No')
  exit()


dfs(sg[0])
if visited.count(True) == N+1:
  print('Yes')
else:
  print('No')

