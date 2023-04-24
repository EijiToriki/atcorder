N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

if A[0] != 0:
    print(0)
    exit()

ans = 1
for i in range(1, N):
    if A[i] - A[i-1] == 0:
        pass
    elif A[i] - A[i-1] == 1:
        ans += 1
    else:
        break

if ans > K:
    ans = K

print(ans)
