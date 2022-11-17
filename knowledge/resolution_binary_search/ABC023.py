N = int(input())
H, S = [], []
for _ in range(N):
  h, s = map(int, input().split())
  H.append(h)
  S.append(s)

left = 0
right = 10**14

while right-left > 1:
  mid = (left + right) // 2
  ok = True
  
  t = [0] * N
  for i in range(N):
    if mid < H[i]:
      ok = False
    else:
      t[i] = (mid - H[i]) // S[i]
    
  t = sorted(t)
  for i in range(N):
    if t[i] < i:
      ok = False
  
  if ok:
    right = mid
  else:
    left = mid

print(right)