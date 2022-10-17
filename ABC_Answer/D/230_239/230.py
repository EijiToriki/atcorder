from operator import itemgetter

N, D = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]
LR.sort(key=itemgetter(1))  # Rでソート

ans = 0
x = 0

for l, r in LR:
  if x < l:
    ans += 1        # パンチの回数
    x = r + D - 1   # 衝撃はで壊せる範囲（問題文参照）

print(ans)
