from collections import defaultdict

def sorted_by_day(medicine_cnt_dict):
  return dict(sorted(medicine_cnt_dict.items()))

def calc_total_medicine(medicine_cnt_dict):
  total_medicine = 0
  for medicine_cnt in medicine_cnt_dict.values():
    total_medicine += medicine_cnt
  return total_medicine

def medicine_below_K(medicine_cnt_dict, total_medicine, K):
  if total_medicine <= K:
    return 1
  
  for day, medicine_cnt in medicine_cnt_dict.items():
    total_medicine -= medicine_cnt
    if total_medicine <= K:
      return day + 1


N, K = map(int, input().split())
medicine_cnt_dict = defaultdict(int)
total_medicine = 0
for _ in range(N):
  a, b = map(int, input().split())
  medicine_cnt_dict[a] += b

medicine_cnt_dict = sorted_by_day(medicine_cnt_dict)
total_medicine = calc_total_medicine(medicine_cnt_dict)
ans = medicine_below_K(medicine_cnt_dict, total_medicine, K)
print(ans)



