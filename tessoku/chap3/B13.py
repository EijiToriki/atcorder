N, K = map(int, input().split())
A = list(map(int, input().split()))

cumsum = [0] * (N+1)
for i in range(1, N+1):
  cumsum[i] = cumsum[i-1] + A[i-1]

ans = 0
r = 1
for l in range(N):
  while r < N+1 and cumsum[r] - cumsum[l] <= K:
    r += 1
  r -= 1
  
  ans += (r-l)
    
print(ans)