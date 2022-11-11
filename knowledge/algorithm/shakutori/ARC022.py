N = int(input())
A = list(map(int, input().split()))

ans = 0
r = 0
snack_set = set()
for l in range(N):
  while r < N and A[r] not in snack_set:
    snack_set.add(A[r])
    r += 1
  
  snack_set.remove(A[l])
  if l == r:
    r += 1
  else:
    ans = max(ans, r-l)

print(ans)