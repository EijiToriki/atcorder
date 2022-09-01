N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = [-1 for _ in range(N)]
for i in range(N):
  num_stack = [P[i]]
  for j in range(i+1, N):
    if len(num_stack) == K:
      for num in num_stack:
        ans[num] = j+1
      break
    