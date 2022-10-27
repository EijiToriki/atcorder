from itertools import chain


H, W = map(int, input().split())
C = []
for _ in range(H):
  C.append(input())

visited = [[False] * W for _ in range(H)]
depth = [[0] * W for _ in range(H)]

dx = [0, 1]
dy = [1, 0]

def dfs(h, w, d):
  visited[h][w] = True
  depth[h][w] = d + 1

  for i in range(2):
    nh = h + dx[i]
    nw = w + dy[i]

    if nh < 0 or nh >= H or nw < 0 or nw >= W:
      continue
    if C[nh][nw] == '#':
      continue
    if visited[nh][nw]:
      continue
    
    dfs(nh, nw, depth[h][w])


dfs(0, 0, 0)

print(max(list(chain(*depth))))