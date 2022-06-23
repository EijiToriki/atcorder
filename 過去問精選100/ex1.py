## 全探索
while True:
  result_cnt = 0
  n, x = map(int, input().split())
  if n==0 and x==0:
    break
  for i in range(1,n+1):
    for j in range(i+1,n+1):
      for k in range(j+1,n+1):
        if i+j+k == x and i != k and j != k and i != j:
          result_cnt +=1
    
  print(result_cnt)