from bisect import bisect_left
from collections import defaultdict

N = int(input())
XY = []
for _ in range(N):
    xy = list(map(int, input().split()))
    XY.append(xy)

xy_dict = defaultdict(list)
XY.sort(key=lambda x:x[0])
Y = [0]
for xy in XY:
    xy_dict[xy[0]].append(xy[1])

for y in xy_dict.values():
    y = sorted(y, reverse=True)
    Y.extend(y)

dp = [1] * (N+1)
L = [0] + [10**18] * N

dp[1] = 1
L[1] = Y[1]
for i in range(2, N+1):
    l_idx = bisect_left(L, Y[i])    
    dp[i] = l_idx
    L[l_idx] = Y[i]

ans = max(dp)
print(ans)
