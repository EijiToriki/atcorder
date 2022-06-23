# いもす法による解法
## データの入力
import sys

input = sys.stdin.readline
n = int(input())

## ステップ1：加算処理
### 区間[a, b] に v を加算したいとき
### a 番目の値に v を加算する
### b+1 番目の値に -v 加算する
product_num = 1000000
data = [0] * (product_num+1)

for i in range(n):
  a, b = map(int, input().split())
  data[a] += 1
  if b+1 < product_num+1:
    data[b+1] -= 1

## ステップ2：累積和
### 累積和をすることによって最終結果が得られる（今回は累積和の最大値を取得すればOK）
ans = data[0]
for i in range(product_num):
  data[i+1] += data[i]
  ans = max(ans,data[i+1])

print(ans)