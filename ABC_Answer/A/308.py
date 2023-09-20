def is_sorted_asc(num_list):
  sorted_num_list = sorted(num_list)
  if sorted_num_list == num_list:
    return True
  else:
    return False

def judge_100_to_675(num_list):
  for num in num_list:
    if num < 100 or num > 675:
      return False
  return True

def judge_div25(num_list):
  for num in num_list:
    if num % 25 != 0:
      return False
  return True

S = list(map(int, input().split()))
if is_sorted_asc(S) and judge_100_to_675(S) and judge_div25(S):
  print('Yes')
else:
  print('No')

