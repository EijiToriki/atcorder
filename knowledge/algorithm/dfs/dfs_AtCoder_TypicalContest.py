# pypyではなく，pythonで実行しないと色々バグる

import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())

C = []
for _ in range(H):
    C_W = input()
    C.append(C_W)

visited = [[False] * (W) for _ in range(H)]

start = [-1, -1]
goal = [-1, -1]
for h in range(H):
    for w in range(W):
        if C[h][w] == 's':
            start = [h,w]
        if C[h][w] == 'g':
            goal = [h,w]

move_H = [1, 0, -1, 0]
move_W = [0, 1, 0, -1]

def dfs(h, w):
    visited[h][w] = True

    for i in range(4):
        move_h, move_w = h + move_H[i], w + move_W[i]

        if move_h < 0 or move_h >= H or move_w < 0 or move_w >= W:
            continue
        if visited[move_h][move_w]:
            continue
        if C[move_h][move_w] == "#":
            continue
        
        dfs(move_h, move_w)

dfs(start[0], start[1])

if visited[goal[0]][goal[1]]:
    print('Yes')
else:
    print('No')
