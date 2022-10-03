N, S = map(int, input().split())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for s in range(S+1):
        if dp[i][s] == 1:
            if s + A[i] <= S:
                dp[i+1][s + A[i]] = 1
            if s + B[i] <= S:
                dp[i+1][s + B[i]] = 1

if dp[N][S] == 0:
    print('No')
else:
    ans = ""
    now = S
    for i in range(N-1, -1, -1):
        if dp[i][now-A[i]] == 1:
            now = now - A[i]
            ans += 'H'
        elif dp[i][now-B[i]] == 1:
            now = now - B[i]
            ans += 'T'
    print('Yes')
    print(''.join(list(reversed(ans))))


