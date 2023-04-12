from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = []
for _ in range(R):
    maze.append(input())

sy, sx = sy-1, sx-1
gy, gx = gy-1, gx-1

dist = [[-1] * C for _ in range(R)]
dist[sy][sx] = 0
que = deque()

que.append([sy, sx])

move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]
while(len(que)!=0):
    v = que.popleft()
    for i in range(4):
        nv = [v[0]+move_y[i], v[1]+move_x[i]]
        if maze[nv[0]][nv[1]] == '#':
            continue
        if dist[nv[0]][nv[1]] != -1:
            continue
        if nv[0] < 0 or nv[0] >= R or nv[1] < 0 or nv[1] >= C:
            continue
        dist[nv[0]][nv[1]] = dist[v[0]][v[1]] + 1
        que.append(nv)

ans = dist[gy][gx]
print(ans)

