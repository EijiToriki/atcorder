import sys
from math import isclose, sqrt
from collections import deque

N = int(input())
sx, sy, tx, ty = map(int, input().split())

C = []
for _ in range(N):
    C.append(list(map(int, input().split())))

S = []
T = []
for i in range(N):
    if (sx-C[i][0]) ** 2 + (sy-C[i][1]) ** 2 == C[i][2] ** 2:
        S.append(i)
    if (tx-C[i][0]) ** 2 + (ty-C[i][1]) ** 2 == C[i][2] ** 2:
        T.append(i)

G = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        d = (C[i][0] - C[j][0]) ** 2 + (C[i][1] - C[j][1]) ** 2

        if (C[i][0]-C[j][0])**2 + (C[i][1]-C[j][1])**2 < (C[i][2]-C[j][2]) **2:
            None
        elif (C[i][0]-C[j][0])**2 + (C[i][1]-C[j][1])**2 > (C[i][2]+C[j][2]) **2:
            None
        else:
            G[i].append(j)
            G[j].append(i)

for s in S:
    visited_set = set()
    visited_set.add(s)
    q = deque()
    q.append(s)
    while len(q) != 0:
        v = q.popleft()
        for node in G[v]:
            if node not in visited_set:
                visited_set.add(node)
                q.append(node)

    for t in T:
        if t in visited_set:
            print('Yes')
            sys.exit()

print('No')
