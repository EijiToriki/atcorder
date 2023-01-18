import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
C = [input() for _ in range(H)]
visited = [[False]*W for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(sx, sy, px, py):
  if sx == px and sy == py and visited[px][py] == True:
    return 0
  visited[px][py] = True

  ret = -10000
  for i in range(4):
    nx, ny = px + dx[i], py + dy[i]
    if nx < 0 or ny < 0 or nx >= H or ny >= W:
      continue
    if C[nx][ny] == '#':
      continue
    if (sx != nx or sy != ny) and visited[nx][ny] == True:
      continue
    v = dfs(sx, sy, nx, ny)
    ret = max(ret, v + 1)
  visited[px][py] = False
  return ret

ans = -1
for i in range(H):
  for j in range(W):
    visited = [[False]*W for _ in range(H)]
    ans = max(ans, dfs(i, j, i, j))

if ans <= 2:
  print(-1)
else:
  print(ans)