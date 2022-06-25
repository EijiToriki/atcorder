N = int(input())
A, B, C = map(int, input().split())

ans = 9999
coin_limit = 9999

for i in range(coin_limit+1):
    for j in range(coin_limit+1-i):
        if (N-A*i-B*j)%C == 0:
            k = (N-A*i-B*j)/C
            if k >= 0:
                ans = min(ans, i+j+k)

print(int(ans))