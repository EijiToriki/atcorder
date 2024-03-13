from collections import defaultdict

N, H, X = map(int, input().split())
P = list(map(int, input().split()))

can_ans = defaultdict(int)
for i in range(N):
  if H + P[i] >= X:
    can_ans[i+1] = P[i]
  
ans = -1
min = 1000
for idx, val in can_ans.items():
  if min > val:
    min = val
    ans = idx

print(ans)