## 入力受取
N, W = map(int, input().split())
Wei, Val = [0], [0]
for _ in range(N):
    w, v = map(int, input().split())
    Wei.append(w)
    Val.append(v)

## 変数の事前準備
maxV = 100005
firstW = 10**18
dp = [[firstW] * (maxV) for _ in range(N+1)]

## dp配列の更新
for i in range(1, N+1):
    for j in range(maxV):


