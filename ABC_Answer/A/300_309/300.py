N, A, B = map(int, input().split())
C = list(map(int, input().split()))

Ci = A + B
ans = -1
for i in range(N):
    if C[i] == Ci:
        ans = i + 1
        break

print(ans)