import sys
import bisect

N = int(input())
A = list(map(int, input().split()))

div10 = sum(A) // 10                # 探す値
if sum(A) % 10 != 0:
    print('No')
    sys.exit()

# N番目からの連続を数えるためにリストを2倍する必要がある
for i in range(len(A)):
    A.append(A[i])

B = [0] * len(A)

B[0] = A[0]
for i in range(len(A)-1):
    B[i+1] = B[i] + A[i+1]

for i in range(N):
    index = bisect.bisect_left(B, div10+B[i])
    if B[index] - B[i] == div10:
        print('Yes')
        sys.exit()

print('No')