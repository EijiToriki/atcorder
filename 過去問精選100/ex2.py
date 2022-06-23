## 全探索
N = int(input())
result_cnt = 0
for i in range(1,N+1,2):
  yakusu_cnt = 0
  for j in range(1,i+1):
    if i%j == 0:
      yakusu_cnt += 1
  if yakusu_cnt == 8:
    result_cnt += 1

print(result_cnt)
