A, B = map(int, input().split())

ans = 0
while True:
    if A == B:
        break
    elif A < B:
        if B % A == 0:
            ans += B // A - 1
            B = B - A * (B // A - 1)
        else:
            ans += B // A
            B = B % A
    else:
        if A % B == 0:
            ans += A // B - 1
            A = A - B * (A // B - 1)
        else:
            ans += A // B
            A = A % B

print(ans)