import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A = list(set(A))
A = sorted(A)

for _ in range(Q):
    b = int(input())
    index = bisect.bisect_left(A, b)
    if index == len(A):
        complain = abs(b-A[index-1])
    else:
        complain = min(abs(b-A[index-1]), abs(b-A[index]))
    print(complain)