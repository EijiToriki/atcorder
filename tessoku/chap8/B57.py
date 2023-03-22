dp_magic_num = 30

N, K = map(int, input().split())

dp = [[0 for _ in range(N+1)] for _ in range(dp_magic_num)]

for i in range(1, N+1):
    strN = str(i)
    keta_wa = 0
    for n in strN:
        keta_wa += int(n)
    dp[0][i] = i - keta_wa

for d in range(1, dp_magic_num):
    for i in range(1, N+1):
        dp[d][i] = dp[d-1][dp[d-1][i]]

binK = bin(K)[2:]
for i in range(1, N+1):
    n = i    
    len_K = len(binK)
    for j, bin in enumerate(binK):
        if bin == '1':
            n = dp[len_K-j-1][n]
    print(n)

