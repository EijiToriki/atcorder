from bisect import bisect_left, bisect_right

def judge(mid):
  seller = bisect_right(A, mid)
  buyer = M - bisect_left(B, mid)
  return seller >= buyer


N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ng = 0
ok = 10**9 + 1
while abs(ok -ng) > 1:
  mid = (ok + ng) // 2
  if judge(mid):
    ok = mid
  else:
    ng = mid

print(ok)