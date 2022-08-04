N = int(input())

dp = [0 for _ in range(N)]


pre_max_index = -1
for i in range(N):
  happiness = list(map(int, input().split()))
  max_val = 0
  max_index = -1

  for j in range(3):
    if j != pre_max_index:
      if max_val < happiness[j]:
        max_val = happiness[j]
        max_index = j
      elif max_val == happiness[j]:
        max_index = -1

  pre_max_index = max_index
  dp[i] = dp[i-1] + max_val

print(dp[N-1])