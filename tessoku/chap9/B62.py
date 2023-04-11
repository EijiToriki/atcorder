import sys
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N+1)
visited[0] = True
ans = []
def dfs(node):
    ans.append(node)

    if node == N:
        print(*ans, sep=' ')
        exit()

    visited[node] = True
    for to in G[node]:
        if visited[to] == False:
            dfs(to)
    ans.pop()

dfs(1)

