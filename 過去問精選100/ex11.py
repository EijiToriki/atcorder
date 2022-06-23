## ビット探索

N, M = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(M)]
p = [int(i) for i in input().split()]

lighting_ptn = 2**N

result = 0

for i in range(lighting_ptn):
  on_light_cnt = 0
  for light_no in range(M):
    on_sw_cnt = 0
    for j in range(N):
      if((i >> j) & 1): ## onの時
        if (j+1) in ks[light_no][1:]:
          on_sw_cnt += 1
    if on_sw_cnt % 2 == p[light_no]:
      on_light_cnt += 1
  if on_light_cnt == M:
    result += 1
  
print(result)
