N, L = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = input().split()
    A.append(int(a))
    B.append(b)

ans = 0
for a, b in zip(A, B):
    if b == 'E':
        ans = max(ans, L-a)
    else:
        ans = max(ans, a)

print(ans)