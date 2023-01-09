from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
cnt = 0
r = 0
map_dict = defaultdict(int)
for l in range(N):
  while r < N:
    if map_dict[A[r]] == 0 and cnt == K:
      break
    if map_dict[A[r]] == 0:
      cnt += 1
    map_dict[A[r]] += 1
    r += 1
  ans = max(ans, r - l)
  if map_dict[A[l]] == 1:
    cnt -= 1
  map_dict[A[l]] -= 1

print(ans)
