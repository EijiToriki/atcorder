N = int(input())
txa = [list(map(int, input().split())) for _ in range(N)]
max_time = txa[N-1][0]

dp = [[0 for _ in range(5)] for _ in range(max_time+1)]

h = 0
for i in range(1, max_time+1):
  if i == txa[h][0]:
    for j in range(min(i+1, 5)):
      if j == txa[h][1]:
        if j == 0:
          dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j+1]) + txa[h][2]
        elif j == 4:
          dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j]) + txa[h][2]
        else:
          dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + txa[h][2]

      if j == 0:
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j+1])
      elif j == 4:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j])
      else:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
    h += 1
  else:
    for j in range(min(i+1, 5)):
      if j == 0:
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j+1])
      elif j == 4:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j])
      else:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

print(max(dp[max_time]))  
