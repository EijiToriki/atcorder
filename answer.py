from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

visited = [False] * (N+1)

def dfs(v, p):
    visited[v] = True

    for next in G[v]:
        if next == p:
            continue
        if visited[next]:
            continue
        dfs(next, v)


ans = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, -1)
    ans += visited.count(True) - 1

ans -= M

print(ans)
