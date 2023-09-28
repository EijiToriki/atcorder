from collections import defaultdict


def get_first_ABC_idx(N, ABC_str):
  ABC_cnt_dict = defaultdict(int)
  for i in range(N):
    ABC_cnt_dict[ABC_str[i]] += 1
    if is_ABC_one_over(ABC_cnt_dict):
      return i+1
  return -1


def is_ABC_one_over(ABC_cnt_dict):
  if ABC_cnt_dict['A'] >= 1 and ABC_cnt_dict['B'] >= 1 and ABC_cnt_dict['C'] >= 1:
    return True
  else:
    return False


N = int(input())
S = input()

ans = get_first_ABC_idx(N, S)
print(ans)