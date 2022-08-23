import sys

H, W = map(int, input().split())
G = [input() for _ in range(H)]

point = [0,0]
visit_point = [[False for _ in range(W)] for _ in range(H)]

while True:
  # 終了条件
  if visit_point[point[0]][point[1]] == True:
    print(-1)
    sys.exit()

  # 移動
  visit_point[point[0]][point[1]] = True
  if G[point[0]][point[1]] == 'U' and point[0] != 0:
    point[0] -= 1
  elif G[point[0]][point[1]] == 'D' and point[0] != H-1:
    point[0] += 1
  elif G[point[0]][point[1]] == 'L' and point[1] != 0:
    point[1] -= 1
  elif G[point[0]][point[1]] == 'R' and point[1] != W-1:
    point[1] += 1
  else:
    break
  
# 添え字で考えていたため，最後に1を加算する
point[0] += 1
point[1] += 1

print(*point)