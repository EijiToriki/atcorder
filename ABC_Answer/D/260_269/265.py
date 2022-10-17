from bisect import  bisect_left

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0 for _ in range(N+1)]
for i in range(N):
  S[i+1] = S[i] + A[i]

flag = False
for x in range(N):
  y = bisect_left(S, S[x]+P)
  if y>N or S[y] != S[x]+P:
    continue

  z = bisect_left(S, S[y]+Q)
  if z>N or S[z] != S[y]+Q:
    continue

  w = bisect_left(S, S[z]+R)
  if w>N or S[w] != S[z]+R:
    continue

  flag = True

if flag:
  print('Yes')
else:
  print('No')

