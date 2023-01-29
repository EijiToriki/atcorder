N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
r = 1
for l in range(N):
  while r < N and A[r] - A[l] <= K:
    r += 1
  ans += (r - l - 1)
  if l == r:
    r += 1
    
print(ans)