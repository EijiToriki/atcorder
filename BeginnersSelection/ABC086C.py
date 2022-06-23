import sys
N = int(input())

t = [0] * N
x = [0] * N
y = [0] * N

for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())

current_x = 0
current_y = 0
current_t = 0

for i in range(N):
  if abs(x[i]-current_x) + abs(y[i]-current_y) > (t[i]-current_t):  ## 最短距離の合計が所要時間以上なら No（たどり着かない）
    print('No')
    sys.exit()
  elif abs(x[i]-current_x) + abs(y[i]-current_y) < (t[i]-current_t):  ## 最短距離の合計が所要時間以内の処理
    if (t[i]-current_t) % (abs(x[i]-current_x) + abs(y[i]-current_y) + 2) != 0: ## 早めに着いた場合，近くを往復し続ける必要がある 
      print('No')
      sys.exit()

  ## 最短距離の合計が所要時間と同じなら，辿り着けるので何もしない
  current_x = x[i]
  current_y = y[i]
  current_t = t[i]

print('Yes')