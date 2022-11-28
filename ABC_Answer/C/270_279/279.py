from collections import defaultdict

H, W = map(int, input().split())
S, T = [], []
for _ in range(H):
  S.append(input())

for _ in range(H):
  T.append(input())

S = sorted(list(zip(*S)))
T = sorted(list(zip(*T)))

if S == T:
  print('Yes')
else:
  print('No')