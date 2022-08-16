R, C = map(int, input().split())

point = [0,14]
color = ['black', 'white']
grid = [['' for _ in range(15)] for _ in range(15)]

for i in range(8):
  now_color = color[i%2]
  for j in range(point[0], point[1]+1):
    grid[point[0]][j] = now_color
    grid[j][point[0]] = now_color
    grid[point[1]][j] = now_color
    grid[j][point[1]] = now_color
  point[0] += 1
  point[1] -= 1

print(grid[R-1][C-1])