import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

kakutei = [False] * (N+1)
cur = [float('inf')] * (N+1)
cur[1] = 0
Q = []
heapq.heappush(Q, (cur[1], 1))

while len(Q) >= 1:
    pos = heapq.heappop(Q)[1]

    if kakutei[pos] == True:
        continue

    kakutei[pos] = True
    for e in G[pos]:
        if cur[e[0]] > cur[pos] + e[1]:
            cur[e[0]] = cur[pos] + e[1]
            heapq.heappush(Q, (cur[e[0]], e[0]))

for i in range(1, N+1):
    if cur[i] != float('INF'):
        print(cur[i])
    else:
        print(-1)
