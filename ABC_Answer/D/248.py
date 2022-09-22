from bisect import bisect, bisect_left
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cnt_dict = defaultdict(list)
for i in range(N):
    cnt_dict[A[i]].append(i+1)

for i in range(Q):
    L, R, X = map(int, input().split())
    print(bisect(cnt_dict[X], R) - bisect_left(cnt_dict[X], L))