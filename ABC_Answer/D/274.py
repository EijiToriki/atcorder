N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
base = 10**4 + 1


dp_x = [[0] * (2*(base-1) + 3) for _ in range(N//2+1)]
dp_x[0][base + A[0]] = 1

dp_y = [[0] * (2*(base-1) + 3) for _ in range(N//2+1)]
dp_y[0][base + A[1]] = 1
dp_y[0][base - A[1]] = 1


for i in range(2, N, 2):
    for x in range(len(dp_x[i//2 - 1])):
        if dp_x[i//2 - 1][x] == 1:
            dp_x[i//2][x + A[i]] = 1
            dp_x[i//2][x - A[i]] = 1

for i in range(3, N, 2):
    for y in range(len(dp_y[i//2 - 1])):
        if dp_y[i//2-1][y] == 1:
            dp_y[i//2][y + A[i]] = 1
            dp_y[i//2][y - A[i]] = 1


if N%2 == 0:
    if dp_x[N//2 - 1][base + X] and dp_y[N//2-1][base + Y]:
        print('Yes')
    else:
        print('No')
else:
    if dp_x[N//2][base + X] and dp_y[N//2-1][base + Y]:
        print('Yes')
    else:
        print('No')