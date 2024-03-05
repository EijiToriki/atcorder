from collections import deque

N, M = map(int, input().split())
A, B = [], []
for _ in range(M):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

stronger = []
weak_set = set()
for h in range(1, N+1):
  weaker = deque([h])
  while len(weaker) != 0:
    person = weaker.popleft()
    for i in range(M):
      if person == A[i] and B[i] not in weak_set:
        weaker.append(B[i])
        weak_set.add(B[i])
    if len(weak_set) == N-1:
      print(h)
      exit()

print(-1)