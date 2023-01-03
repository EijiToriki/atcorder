N = int(input())
A = list(map(int, input().split()))

one, two, three = A.count(1), A.count(2), A.count(3)

dp = [[[-1] * (N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 0


def f(i, j, k):
  if dp[i][j][k] >= 0:
    return dp[i][j][k]
  res = N / (i + j + k)
  if i-1 >= 0:
    res += f(i-1, j, k) * i / (i + j + k)
  if j-1 >= 0:
    res += f(i+1, j-1, k) * j / (i + j + k)
  if k-1 >= 0:
    res += f(i, j+1, k-1) * k / (i + j + k)
  dp[i][j][k] = res
  return res

ans = f(one, two, three)
print(ans)