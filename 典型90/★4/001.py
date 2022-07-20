N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)

dif = [A[0]]  # 切り口の差
for i in range(N):
  dif.append(A[i+1]-A[i])

def is_ok(x):
  length = 0
  cnt = 0
  for i in dif:
    length += i
    if length >= x:
      length = 0
      cnt += 1
  return cnt


def my_bisect(ng, ok):
  while ng - ok > 1:
    mid = (ng + ok) // 2
    if is_ok(mid) >= K + 1:   # まだ大きくできる
      ok = mid
    else:
      ng = mid                # 小さくしなければならない
  return ok

print(my_bisect(L+1, -1))