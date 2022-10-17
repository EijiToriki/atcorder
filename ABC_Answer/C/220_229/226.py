N = int(input())
T = []
K = []
A = []
for _ in range(N):
  row = list(map(int, input().split()))
  T.append(row[0])
  K.append(row[1])
  A.append(row[2:])
  
dp = [0 for _ in range(N)]

for i in range(N):
  if len(A) == 0:
    dp[i] = T[i]
  else:
    for j in range(K[i]):
      dp[i] += dp[A[i][j]-1]
    dp[i] += T[i]

print(dp[N-1])