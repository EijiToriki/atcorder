import sys

def is_ok(mid, ok, eq):
    if S[mid] - S[ok] == eq:
        return True
    else:
        return False

def binary_search(ok, ng, eq):
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, ok, eq):
            ok = mid
        else:
            ng = mid
    return ok

def get_index(x, eq):
  result = -1
  for i in range(x, N+1):
    idx = binary_search(i,N,eq)
    if S[idx] - S[i] == eq:
      result = idx
      break

  if result == -1:
    print('No')
    sys.exit()
  else:
    return result

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0 for _ in range(N+1)]
for i in range(N):
  S[i+1] = S[i] + A[i]

x = 0
y = get_index(x, P)
z = get_index(y, Q)
w = get_index(z, R)

print('Yes')




