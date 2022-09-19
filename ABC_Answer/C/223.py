N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

total_time = 0
for i in range(N):
    total_time += A[i] / B[i]

half_time = total_time / 2

ans = 0
check_time = [0] * (N+1)
for i in range(N):
    check_time[i+1] = check_time[i] + A[i] / B[i]
    if check_time[i+1] > half_time:
        between = half_time - check_time[i]
        ans += between * B[i]
        break
    else:
        ans += A[i]

print(ans)
        