N = int(input())
P = list(map(int, input().split()))

op_cnt = [0 for _ in range(N)]
for i in range(len(P)):
  op_cnt[(N-P[i]+i-1)%N] += 1
  op_cnt[(N-P[i]+i)%N] += 1
  op_cnt[(N-P[i]+i+1)%N] += 1

print(max(op_cnt))