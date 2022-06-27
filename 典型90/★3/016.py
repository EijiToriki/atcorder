N = int(input())
A, B, C = map(int,input().split())

max_coin = 9999
ans = max_coin

for i in range(max_coin+1):
    for j in range(max_coin+1-i):
        if (N-A*i-B*j) % C == 0:
            k = (N-A*i-B*j) // C 
            if k >= 0 and i+j+k < ans:
                ans = i+j+k

print(ans)