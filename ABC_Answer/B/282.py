N, M = map(int, input().split())
S = []

for _ in range(N):
  s = input()
  S.append(s)

ans = 0
for i in range(N):
  for j in range(i+1, N):
    can_answer = 0
    for k in range(M):
      if S[i][k] == 'o' or S[j][k] == 'o':
        can_answer += 1
    if can_answer == M:
      ans += 1

print(ans)

