def get_Tak_Code(N, M, grid):
  tak_code_region = []
  for i in range(N-8):
    for j in range(M-8):
      if judge_Tak_Code(i, j, grid):
        tak_code_region.append((i+1, j+1))

  return tak_code_region

def judge_Tak_Code(i, j, grid):
  if judge_must_black(i, j, grid) and judge_must_white(i, j, grid):
    return True
  else:
    return False

def judge_must_black(i, j, grid):
  for x in range(3):
    for y in range(3):
      if grid[i+x][j+y] != '#':
        return False

  for x in range(3):
    for y in range(3):
      if grid[i+6+x][j+6+y] != '#':
        return False

  return True

def judge_must_white(i, j, grid):
  for left_y in range(4):
    if grid[i+3][j+left_y] != '.':
      return False
  
  for left_x in range(4):
    if grid[i+left_x][j+3] != '.':
      return False
  
  for right_y in range(4):
    if grid[i+5][j+5+right_y] != '.':
      return False
  
  for right_x in range(4):
    if grid[i+5+right_x][j+5] != '.':
      return False
  
  return True


def print_ans(anses):
  for ans in anses:
    print(*ans)

N, M = map(int, input().split())
S = []
for _ in range(N):
  S.append(input())

anses = get_Tak_Code(N, M, S)
anses = sorted(anses, key=lambda x:(x[0], x[1]))
print_ans(anses)