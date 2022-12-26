N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    k = query[1] - 1
    x = query[2]
    A[k] = x
  else:
    k = query[1] - 1
    print(A[k])
