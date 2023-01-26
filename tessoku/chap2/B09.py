N = int(input())
maxXY = 1510
cumsum = [[0] * maxXY for _ in range(maxXY)]

for _ in range(N):
  a, b, c, d = map(int, input().split())
  cumsum[a][b] += 1
  cumsum[c][d] += 1
  cumsum[a][d] -= 1
  cumsum[c][b] -= 1

for h in range(maxXY):
  for w in range(1, maxXY):
    cumsum[h][w] += cumsum[h][w-1]

for w in range(maxXY):
  for h in range(1, maxXY):
    cumsum[h][w] += cumsum[h-1][w]

## クエリへの回答
ans = 0
for x in range(maxXY):
  for y in range(maxXY):
    if cumsum[x][y] >= 1:
      ans += 1

print(ans)