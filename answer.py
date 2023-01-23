N, A, B = map(int, input().split())
S = list(input()) * 2

ans = 10**18
for i in range(N):
  cost = A * i
  for j in range(N//2):
    if S[i+j] != S[N+i-j-1]:
      cost += B
  ans = min(ans, cost)

print(ans)

