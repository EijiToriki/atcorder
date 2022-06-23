## 2分探索
import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

large_parts_cnt = 0

for i in range(N):
  large_parts_cnt += (N-bisect.bisect(C,B[i])) * bisect.bisect_left(A,B[i])

print(large_parts_cnt)