from operator import itemgetter

N, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB = sorted(AB, key=itemgetter(0), reverse=True)

ans = 0
w = 0
for ab in AB:
  w += ab[1]
  if w < W:
    ans += ab[0] * ab[1]
  else:
    ans += ab[0] * (W - (w - ab[1])) 
    break

print(ans)