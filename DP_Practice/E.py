# 価値でDP配列を作る
from collections import defaultdict

N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

dp = defaultdict(int)

for n in range(N):
  if n == 0:
    dp[wv[n][0]] = wv[n][1]
  else:
    dp_copy = dp.copy()
    dp[wv[n][0]] = wv[n][1]
    for w, v in dp_copy.items():
      if w + wv[n][0] <= W:
        dp[wv[n][0] + w] = max(dp[wv[n][0] + w], dp[w] + wv[n][1])

print(max(dp.values()))