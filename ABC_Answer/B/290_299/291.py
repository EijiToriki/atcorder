N = int(input())
X = list(map(int, input().split()))

X = sorted(X)

total = sum(X)
for i in range(N):
    total -= (X[i] + X[-(i+1)])

man_num = 5 * N - 2 * N
ans = total / man_num
print(ans)

