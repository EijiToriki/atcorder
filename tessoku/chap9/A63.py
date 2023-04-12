from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [-1] * (N+1)
dist[1] = 0
que = deque()

que.append(1)

while(len(que)!=0):
    v = que.popleft()

    for next in G[v]:
        if dist[next] != -1:
            continue
        dist[next] = dist[v] + 1
        que.append(next)


for v in range(1, N+1):
    print(dist[v])