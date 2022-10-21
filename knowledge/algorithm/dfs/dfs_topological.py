import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

topological = []
visited = [False] * (N)

def dfs(v):
    visited[v] = True
    for next in G[v]:
        if visited[next]:
            continue
        dfs(next)
    
    topological.append(v)

for i in range(N):
    if visited[i]:
        continue
    dfs(i)

print(topological)
for i in reversed(topological):
    print(i, end=" ")