N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [float('inf')] * (N+1)
dp[0], dp[1] = 0, 0
dp[2] = A[2]

for i in range(3, N+1):
  dp[i] = min(dp[i], dp[i-1] + A[i], dp[i-2] + B[i])

ans = []
i = N
while True:
    if dp[i] == dp[i-1] + A[i]:
        i = i - 1
        ans.append(i)
    elif dp[i] == dp[i-2] + B[i]:
        i = i -2
        ans.append(i)
    
    if i <= 0 or dp[i] == 0:
        break

ans = list(reversed(ans))
ans.append(N)

print(len(ans))
print(*ans)