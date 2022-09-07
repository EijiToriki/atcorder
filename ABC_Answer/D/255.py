N, Q = map(int, input().split())
A = list(map(int, input().split()))
 
for i in range(Q):
    x = int(input())
    ans = 0
    for a in A:
         ans += abs(a-x)
    print(ans)