import sys
sys.setrecursionlimit(10**6)

N, T = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [-1] * (N+1)
ans = [0] *(N+1)

def dfs(p):
    visited[p] = True
    ans[p] = 0

    for next in G[p]:
        if visited[next] == True:
            continue
        ret = dfs(next)
        ans[p] = max(ans[p], ret + 1)

    return ans[p]

dfs(T)
print(*ans[1:])
