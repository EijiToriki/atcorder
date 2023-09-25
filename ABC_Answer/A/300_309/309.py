def is_group_div3(a, b):
  if (a-1) // 3 == (b-1) // 3:
    return True
  else:
    return False

def is_abs_diff1(a, b):
  if abs(a-b) == 1:
    return True
  else:
    return False


A, B = map(int, input().split())
if is_group_div3(A, B) and is_abs_diff1(A, B):
  print('Yes')
else:
  print('No')

