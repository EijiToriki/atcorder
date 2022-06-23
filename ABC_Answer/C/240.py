N, X = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*ab)]

dp = [[0 for _ in range(X+1)] for _ in range(N+1)]

if A[0] <= X:
  dp[1][A[0]] = 1
if B[0] <= X:
  dp[1][B[0]] = 1

for i in range(2,N+1):
  for j in range(1,X+1):
    if dp[i-1][j] == 1:
      jumpA = j + A[i-1]
      jumpB = j + B[i-1] 
      if jumpA <= X:
        dp[i][jumpA] = 1
      if jumpB <= X:
        dp[i][jumpB] = 1

if dp[N][X] == 1:
  print("Yes")
else:
  print("No")
