H, W = map(int, input().split())
X = [[0] * (W+1)]
for _ in range(H):
  x = list(map(int, input().split()))
  x = [0] + x
  X.append(x)

## 2次元累積和の事前準備
cumsum = [[0] * (W+1) for _ in range(H+1)]
for h in range(1, H+1):
  cumsum[h][1] = X[h][1]

for h in range(1, H+1):
  for w in range(2, W+1):
    cumsum[h][w] = cumsum[h][w-1] + X[h][w]

for w in range(W+1):
  for h in range(2, H+1):
    cumsum[h][w] += cumsum[h-1][w]

## クエリへの回答
Q = int(input())
for _ in range(Q):
  a, b, c, d = map(int, input().split())
  ans = cumsum[c][d] - cumsum[a-1][d] - cumsum[c][b-1] + cumsum[a-1][b-1]
  print(ans)
