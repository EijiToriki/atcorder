from statistics import median

N = int(input())
X, Y = [], []
for _ in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

x_med = median(X)
y_med = median(Y)

ans = 0
for x, y in zip(X, Y):
  ans += abs(x-x_med)
  ans += abs(y-y_med)

print(int(ans))
