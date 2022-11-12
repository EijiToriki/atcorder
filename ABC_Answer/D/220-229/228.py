Q = int(input())
N = 2**20
A = [-1] * N
P = [h for h in range(N)]

for _ in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    h = x % N
    p = h
    visited = [p]
    while A[p] != -1: 
      p = P[p]
      visited.append(p)
    A[p] = x
    new_p = P[(p+1) % N]
    for u in visited:
      P[u] = new_p
  else:
    print(A[x%N])