N, K = map(int, input().split())
S = []
for _ in range(N):
  S.append(int(input()))

if 0 in S:
  print(N)
  exit()

ans = 0
r = 0
multi = 1
for l in range(N):
  while r < N and multi * S[r] <= K:
    multi *= S[r]
    r += 1
  
  if l == r:
    r += 1
  else:
    multi //= S[l]
    ans = max(ans, r-l)

print(ans)