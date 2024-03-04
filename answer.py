from collections import deque

N, M = map(int, input().split())
A, B = [], []
for _ in range(M):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

stronger = []
for h in range(1, N+1):
  weaker = deque([h])
  weak_set = set((h,))
  while len(weaker) != 0:
    person = weaker.popleft()
    for i in range(M):
      if person == A[i]:
        weaker.append(B[i])
        weak_set.add(B[i])
    if len(weak_set) == N:
      stronger.append(h)
      break

if len(stronger) == 1:
  print(stronger[0])
else:
  print(-1)