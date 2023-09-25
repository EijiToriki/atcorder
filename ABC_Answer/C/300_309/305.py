H, W = map(int, input().split())
S = []
for _ in range(H):
  S.append(input())

cookie_x = []
cookie_y = []

flag = False
for i in range(H):
  for j in range(W):
    if S[i][j] == "#":
      cookie_x.append(i)
      cookie_y.append(j)
      flag = True
      break
  if flag:
    break

flag = False
for i in range(H):
  for j in range(W-1, 0, -1):
    if S[i][j] == "#":
      cookie_x.append(i)
      cookie_y.append(j)
      flag = True
      break
  if flag:
    break

flag = False
for i in range(H-1, 0, -1):
  for j in range(W):
    if S[i][j] == "#":
      cookie_x.append(i)
      cookie_y.append(j)
      flag = True
      break
  if flag:
    break
  

flag = False
for i in range(H-1, 0, -1):
  for j in range(W-1, 0, -1):
    if S[i][j] == "#":
      cookie_x.append(i)
      cookie_y.append(j)
      flag = True
      break
  if flag:
    break


minX = min(cookie_x)
maxX = max(cookie_x)
minY = min(cookie_y)
maxY = max(cookie_y)

for i in range(minX, maxX+1):
  for j in range(minY, maxY+1):
    if S[i][j] == '.':
      ans = [i+1, j+1]

print(*ans)