import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

val = [i for i in range(N+1)]  # 答えを格納
pos = [i for i in range(N+1)]  # 順番を格納（整数 i が書かれているボールが左から何番目にあるかを pos[i] で表す）

for i in range(Q):
  x = int(input())
  p0 = pos[x]
  p1 = p0 + 1
  if p0 == N:
    p1 = p0 - 1

  val[p0], val[p1] = val[p1], val[p0]
  pos[val[p0]],pos[val[p1]] = pos[val[p1]],pos[val[p0]]
  

print(*val[1:])