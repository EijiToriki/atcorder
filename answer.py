T = int(input())

for _ in range(T):
    N, D, K = map(int, input().split())
    if D > N:
        D = D % N
    if D == 0:
        D = 1
    if N % 2 == 0:
        if N >= 2 * D:
            ans = D * (K-1) % N + (K-1) // (N // D) % N 
            print(ans)
        else:
            ans = D * (K-1) % N + (K-1) // (N // (N-D)) % N 
            print(ans)
    else:
        ans = D * (K-1) % N
        print(ans)