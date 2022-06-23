## 累積和
N = int(input())
A = list(map(int, input().split()))

cum_sum = [0] + [sum(A[:i+1]) for i in range(len(A))]   ## 累積和の計算

for i in range(1,N+1):
  max_resource_amount = 0
  for j in range(i, N+1):
    resource_amount = cum_sum[j] - cum_sum[j-i]   ## 例：A[4:13]の和が欲しければ，cum_sum[13] - cum_sum[4] を計算すればよい
    if max_resource_amount < resource_amount:
      max_resource_amount = resource_amount
  print(max_resource_amount)