N = int(input())
S, T = [], []
for _ in range(N):
  s, t = input().split()
  S.append(s)
  T.append(t)

check_flag = False
for i in range(N):
  for j in range(i+1, N):
    if S[i] == S[j] and T[i] == T[j]:
      check_flag = True

if check_flag:
  print('Yes')
else:
  print('No')
