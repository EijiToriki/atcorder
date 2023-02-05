N, K = map(int, input().split())
S = []
for i in range(N):
  s = input()
  if i+1 <= K:
    S.append(s)
S = sorted(S)

for s in S:
  print(s)
