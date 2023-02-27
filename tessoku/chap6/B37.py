N = int(input())

power10 = [1]
for i in range(1, 17):
    power10.append(power10[i-1] * 10)

R = [[0] * 10 for _ in range(18)]
for i in range(15):
    digit = (N // power10[i]) % 10
    for j in range(10):
        if j < digit:
            R[i][j] = (N//power10[i+1])*power10[i] + power10[i]
        if j == digit:
            R[i][j] = (N//power10[i+1])*power10[i] + (N % power10[i] + 1)
        if j > digit:
            R[i][j] = (N//power10[i+1])*power10[i]

ans = 0
for i in range(15):
    for j in range(10):
        ans += j * R[i][j]

print(ans)


