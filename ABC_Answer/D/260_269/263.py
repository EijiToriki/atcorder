N, L, R = map(int, input().split())
A = list(map(int, input().split()))

l_score = [0] + [0 for _ in range(N)]
r_score = [0] + [0 for _ in range(N)]
for i in range(N):
  l_score[i+1] = min(l_score[i]+A[i], L*(i+1))
  r_score[i+1] = min(r_score[i]+A[N-i-1], R*(i+1))

ans = float('inf')
for i in range(N+1):
  if l_score[i]+r_score[N-i] < ans:
    ans = l_score[i]+r_score[N-i]

print(ans)