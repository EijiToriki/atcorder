dp_magic_num = 30

N, Q = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(dp_magic_num)]

for i in range(len(A)):
    dp[0][i] = A[i]

for i in range(1, dp_magic_num):
    for j in range(len(A)):
        dp[i][j] = dp[i-1][dp[i-1][j]-1]


for _ in range(Q):
    x, y = map(int, input().split())
    y = bin(y)[2:]
    y_len = len(y)
    for i, bit in enumerate(y):
        if bit == '1':
            x = dp[y_len-i-1][x-1]
    print(x)