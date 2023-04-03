import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N)

def dfs(node):
    visited[node] = True

    for to in G[node]:
        if visited[to] == False:
            dfs(to)
    
dfs(0)
if all(visited):
    print('The graph is connected.')
else:
    print('The graph is not connected.')
