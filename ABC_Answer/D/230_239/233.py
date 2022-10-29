from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N+1)
for i in range(N):
  S[i+1] = S[i] + A[i]

cnt_dict = defaultdict(int)

ans = 0
for i in range(1, N+1):
  cnt_dict[S[i-1]] += 1
  ans += cnt_dict[S[i]-K]


print(ans)