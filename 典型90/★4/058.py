from collections import defaultdict

N, K = map(int, input().split())

if N == 0:
  print(0)
  exit()

## 1～44が10**5を超えたときにどの値に戻ってくるかを辞書にする
loop_dict = defaultdict(int)
for h in range(1, 45):
  x = h
  for i in range(10000):
    str_x = str(x)
    add = 0
    for x_ele in str_x:
      add += int(x_ele)
    if x + add >= 10 ** 5:
      loop_dict[h] = (x + add)%10**5
      break    
    x += add

## 10, 20, 44 のいずれかに戻ってくるので，1回あたりのボタン押下の回数を辞書にする
loop_num_dict = defaultdict(int)
for h in [10, 20, 44]:
  x = h
  for i in range(10000):
    str_x = str(x)
    add = 0
    for x_ele in str_x:
      add += int(x_ele)
    if x + add >= 10 ** 5:
      loop_num_dict[h] = i + 1    ## 超過分の + 1
      break    
    x += add


## 与えられた N で 10**5 を超過するまで回す
x = N
for i in range(K):
  str_x = str(x)
  add = 0
  for x_ele in str_x:
    add += int(x_ele)
  if x + add >= 10 ** 5:
    x = (x + add)%10**5
    break    
  x += add

## 値の超過がなかった場合は，答えを出して終わり
first_loop_num = i + 1
if first_loop_num == K:
  print(x)
  exit()
## 値の超過があった場合の処理が分からん．
## K を引いていく方法だと TLE しそうな感じ
else:
  K = K - first_loop_num
  while True:
    if K - loop_num_dict[loop_dict[x]] < 0:
      break
    else:
      K -= loop_num_dict[loop_dict[x]]
      x = loop_dict[x]
  print(K)
