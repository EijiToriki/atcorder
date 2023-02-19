N = int(input())
S = []
for _ in range(N):
  S.append(input())

for i in range(N-1, -1, -1):
  print(S[i])