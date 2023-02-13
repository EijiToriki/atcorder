N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int, input().split())))
X = int(input())
maxConst = 10 ** 5 + 1

dp = [0] * (maxConst)
for b in B:
    dp[b] = float('inf')

for a in A:
    if dp[a] != float('inf'):
        dp[a] = 1

for i in range(1, maxConst):
    if dp[i] == 1:
        for a in A:
            if i+a < maxConst and dp[i+a] != float('inf'):
                dp[i+a] = 1

if dp[X] == 1:
    print('Yes')
else:
    print('No')