N = int(input())
X1, Y1, X2, Y2 = [], [], [], []
for _ in range(N):
  x1, y1, x2, y2 = map(int, input().split())
  X1.append(x1)
  Y1.append(y1)
  X2.append(x2)
  Y2.append(y2)

plane = [[0] * 1010 for _ in range(1010)]

for i in range(N):
  plane[X1[i]][Y1[i]] += 1
  plane[X1[i]][Y2[i]] -= 1
  plane[X2[i]][Y1[i]] -= 1
  plane[X2[i]][Y2[i]] += 1

for i in range(1001):
  for j in range(1, 1001):
    plane[i][j] += plane[i][j-1]

for i in range(1, 1001):
  for j in range(1001):
    plane[i][j] += plane[i-1][j]

ans = [0] * (N+1)
for i in range(1001):
  for j in range(1001):
    if plane[i][j] >= 1:
      ans[plane[i][j]] += 1

for i in range(1, N+1):
  print(ans[i])

