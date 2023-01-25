N = int(input())
maxX, maxY = 1510, 1510
X, Y = [], []
for _ in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

cumsum = [[0] * maxX for _ in range(maxY)]
## 2次元累積和の事前準備
for x, y in zip(X, Y):
  cumsum[x][y] += 1

for x in range(maxX):
  for y in range(1, maxY):
    cumsum[x][y] += cumsum[x][y-1]

for y in range(maxY):
  for x in range(1, maxX):
    cumsum[x][y] += cumsum[x-1][y]

## クエリへの回答
Q = int(input())
for _ in range(Q):
  a, b, c, d = map(int, input().split())
  ans = cumsum[c][d] - cumsum[a-1][d] - cumsum[c][b-1] + cumsum[a-1][b-1]
  print(ans)

