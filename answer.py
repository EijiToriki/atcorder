from collections import defaultdict

N = int(input())
F, S = [], []
for _ in range(N):
  f, s = map(int, input().split())
  F.append(f)
  S.append(s)

flavor_dict = defaultdict(list)
for f, s in zip(F, S):
  flavor_dict[f].append(s)

maxF, maxS = 0, 0
for f, s in flavor_dict.items():
  if maxS < max(s):
    maxS = max(s)
    maxF = f

flavor_dict[maxF].remove(maxS)
ans = maxS

for f, s in flavor_dict.items():
  if len(s) != 0:
    if f == maxF:
      if ans < maxS + (max(s) // 2):
        ans = maxS + (max(s) // 2)
    else:
      if ans < maxS + max(s):
        ans = maxS + max(s)

print(ans)