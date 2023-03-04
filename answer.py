from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)

ans = [0]

@lru_cache(maxsize=10**6)
def dfs(v, p, pp, d):
    if d == 2:
        if v not in G[pp]:
            ans[0] += 1
            G[pp].append(v)
            return None
    for next in G[v]:
        if next == p:
            continue
        dfs(next, v, p, d+1)
    
for i in range(1, N+1):
    for j in range(1, N+1):
        visited = [False] * (N+1)
        dfs(j, -1, -1, 0)

print(ans[0])
