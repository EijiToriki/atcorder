## いもす法で解く
import sys
 
input = sys.stdin.readline
n = int(input())
 
## ステップ1：加算処理
### 区間[a, b] に v を加算したいとき
### a 番目の値に v を加算する
### b+1 番目の値に -v 加算する
num = 2*(10**5)
data = [0] * (num+1)
 
for i in range(n):
  a, b = map(int, input().split())
  data[a] += 1
  data[b] -= 1
 
## ステップ2：累積和
### 累積和をすることによって最終結果が得られる（今回は累積和の最大値を取得すればOK）
flag = 0
for i in range(num):
  data[i+1] += data[i]
  if data[i+1] != 0 and flag == 0:
    left = i + 1
    flag = 1
  elif data[i+1] == 0 and flag == 1:
    right = i + 1
    flag = 0
    print(left, right)
