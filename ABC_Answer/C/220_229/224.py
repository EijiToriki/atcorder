N = int(input())
XY = []
for _ in range(N):
  XY.append(list(map(int, input().split())))

ans = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      if (XY[j][0]-XY[i][0])*(XY[k][1]-XY[i][1]) != (XY[j][1]-XY[i][1])*(XY[k][0]-XY[i][0]):
        ans += 1

print(ans)