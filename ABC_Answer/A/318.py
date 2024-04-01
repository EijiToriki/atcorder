N, M, P = map(int, input().split())

ans = 0
moon = M
while moon <= N:
  ans += 1
  moon += P

print(ans)