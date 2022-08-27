import sys
# 再帰回数決めないとエラーになる
sys.setrecursionlimit(10**5+10)

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
  x, y = map(int, input().split())
  x, y = x-1, y-1
  G[x].append(y)

dp = [-1] * N
def rec(v):
  if(dp[v] != -1):
    return dp[v]
  
  res = 0
  for nv in G[v]:
    res = max(res, rec(nv) + 1)
    
  dp[v] = res
  return dp[v]


ans = 0
for i in range(N):
  ans = max(ans, rec(i))
print(ans)
