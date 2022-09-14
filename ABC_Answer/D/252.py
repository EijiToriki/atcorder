N = int(input())
A = list(map(int, input().split()))

maxA = max(A)
cnt = [0]*(maxA+1)
for i in range(N):
  cnt[A[i]] += 1

for i in range(maxA):
  cnt[i+1] += cnt[i]

ans = 0
for j in range(N):
  ans += cnt[A[j]-1]*(N-cnt[A[j]])

print(ans)