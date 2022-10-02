N, S = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
card = [['' for _ in range(S+1)] for _ in range(N+1)]

for n in range(N):
    for s in range(1, S+1):
        card[n+1][s] = card[n][s]

    for s in range(1, S+1):
        if dp[n][s] + A[n] <= S:
            dp[n+1][dp[n][s] + A[n]] = dp[n][s] + A[n]
            if len(card[n+1][dp[n][s] + A[n]]) <= n:
                card[n+1][dp[n][s] + A[n]] = card[n][s] + 'H'
                
        if dp[n][s] + B[n] <= S:
            dp[n+1][dp[n][s] + B[n]] = dp[n][s] + B[n]
            if len(card[n+1][dp[n][s] + B[n]]) <= n:
                card[n+1][dp[n][s] + B[n]] = card[n][s] + 'T'

        max_val = max(dp[n][s], dp[n+1][s-1], dp[n+1][s])

        if max_val == dp[n][s]:
            card[n+1][s] = card[n][s]
        elif max_val == dp[n+1][s-1]:
            card[n+1][s] = card[n+1][s-1]

        dp[n+1][s] = max_val

if len(card[N][S]) != N:
    print("No")
else:
    print("Yes")
    print(card[N][S])
