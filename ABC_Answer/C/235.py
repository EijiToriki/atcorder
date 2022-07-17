N, Q = map(int, input().split())
A = list(map(int, input().split()))

A_dict = {}
for i in range(N):
  if A[i] in A_dict:
    A_dict[A[i]].append(i+1)
  else:
    A_dict[A[i]] = [i+1]


for _ in range(Q):
  x,k = map(int, input().split())
  try:
    print(A_dict[x][k-1])
  except IndexError:
    print(-1)
  except KeyError:
    print(-1)

