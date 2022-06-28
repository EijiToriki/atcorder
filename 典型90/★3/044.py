import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

dequeA = deque(A)

for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        dequeA[x-1], dequeA[y-1] = dequeA[y-1], dequeA[x-1]    
    elif T == 2:
        dequeA.appendleft(dequeA[N-1])
    elif T == 3:
        print(dequeA[x-1])