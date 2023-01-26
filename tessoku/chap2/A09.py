H, W, N = map(int, input().split())
maxHW = 1510
cumsum = [[0] * maxHW for _ in range(maxHW)]

for _ in range(N):
  a, b, c, d = map(int, input().split())
  cumsum[a][b] += 1
  cumsum[c+1][d+1] += 1
  cumsum[a][d+1] -= 1
  cumsum[c+1][b] -= 1

for h in range(maxHW):
  for w in range(1, maxHW):
    cumsum[h][w] += cumsum[h][w-1]

for w in range(maxHW):
  for h in range(1, maxHW):
    cumsum[h][w] += cumsum[h-1][w]

## クエリへの回答
for h in range(1, H+1):
  print(*cumsum[h][1:W+1])
