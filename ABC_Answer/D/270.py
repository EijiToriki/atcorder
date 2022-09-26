N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
takahashi = 0
aoki = 0

idx = len(A)-1

while True:
    point = A[idx]
    if cnt % 2 == 0:
        if N - point >= 0:
            takahashi += point
            N = N - point
            cnt += 1
        else:
            idx = idx - 1
    else:
        if N - point >= 0:
            aoki += point
            N = N - point
            cnt += 1
        else:
            idx = idx - 1

    if N == 0:
        break

print(takahashi)
print(aoki)