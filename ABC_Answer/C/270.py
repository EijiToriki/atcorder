from collections import deque

N, X, Y = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = [X]

def dfs(a, b):
    if a == Y:
        print(*ans)
        exit()
    for to in G[a]:
        if to == b:
            continue
        ans.append(to)
        dfs(to, a)
        ans.pop()

dfs(X, False)