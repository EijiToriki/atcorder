N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

a_max = 5
grundy = [0] * a_max
for i in range(a_max):
    transit = [False, False, False]
    if i >= X:
        transit[grundy[i-X]] = True
    if i >= Y:
        transit[grundy[i-Y]] = True
    if transit[0] == False:
        grundy[i] = 0
    elif transit[1] == False:
        grundy[i] = 1
    else:
        grundy[i] = 2

xor_sum = 0
for i in range(N):
    xor_sum = xor_sum ^ grundy[A[i] % 5]

if xor_sum != 0:
    print('First')
else:
    print('Second')
