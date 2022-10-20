import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N+1)


def dfs(n):
    visited[n] = True

    for to in G[n]:
        if visited[to] == False:        
            dfs(to)

ans = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        ans += 1

print(ans)