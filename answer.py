N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [float('inf') for _ in range(N)]
dp[0] = 0

for i in range(1,N):
  dp_ans = float('inf')
  for j in range(1, K+1):
    if i-j < 0:
      break
    else:
      if dp_ans > dp[i-j] + abs(H[i]-H[i-j]):
        dp_ans = dp[i-j] + abs(H[i]-H[i-j])
    
  dp[i] = dp_ans

print(dp[N-1])