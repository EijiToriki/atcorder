def chineseTable(P, N):
  result = 0
  for i in range(len(P)):
    if i==P[i] or (i-1)%N == P[i] or (i+1)%N == P[i]:
      result += 1

  return result


N = int(input())
P = list(map(int, input().split()))
P = P*3

p0 = [i for i, x in enumerate(P) if x == 0][1]

P1 = P[p0:p0+N]
P2 = P[p0-1:p0+N-1]
P3 = P[p0+1:p0+N+1]

ans = 0
ans = max(ans, chineseTable(P1, N))
ans = max(ans, chineseTable(P2, N))
ans = max(ans, chineseTable(P3, N))

print(ans)
