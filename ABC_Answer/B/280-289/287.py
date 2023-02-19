N, M = map(int, input().split())
SN, TM = [], []
for _ in range(N):
  s = input()
  SN.append(s[-3:])

for _ in range(M):
  t = input()
  if t not in TM:
    TM.append(t)

ans = 0
for s in SN:
  for t in TM:
    if s == t:
      ans += 1

print(ans)